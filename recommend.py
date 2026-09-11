import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------
# Load Dataset
# -------------------------
def load_data(file):
    try:
        df = pd.read_csv(file, encoding="cp1252")
    except:
        try:
            df = pd.read_csv(file, encoding="latin1")
        except:
            df = pd.read_csv(file)

    # Convert column names to lowercase
    df.columns = df.columns.str.lower().str.strip()

    # Fix corrupted characters
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("�", "'", regex=False)
            .str.replace("ï¿½", "'", regex=False)
            .str.replace("â€™", "'", regex=False)
            .str.replace("â€œ", '"', regex=False)
            .str.replace("â€\u009d", '"', regex=False)
            .str.replace("â€“", "-", regex=False)
        )

    return df


# -------------------------
# Preprocess Dataset
# -------------------------
def preprocess_data(df):

    df.columns = df.columns.str.lower().str.strip()

    df = df.rename(columns={
        "course name": "course_title",
        "skills": "category",
        "course description": "description",
        "difficulty level": "difficulty_level",
        "course rating": "rating"
    })

    # Fill missing values
    df = df.fillna("")

    # Create tags
    df["tags"] = (
        df["course_title"].astype(str) + " " +
        df["category"].astype(str) + " " +
        df["description"].astype(str) + " " +
        df["difficulty_level"].astype(str)
    )

    df = df[df["tags"].str.strip() != ""]

    return df


# -------------------------
# Build TF-IDF Model
# -------------------------
def build_model(df):

    tfidf = TfidfVectorizer(stop_words="english")

    matrix = tfidf.fit_transform(df["tags"])

    similarity = cosine_similarity(matrix)

    return similarity


# -------------------------
# Recommendation Function
# -------------------------
def recommend(course_name, df, similarity_matrix):

    df = df.reset_index(drop=True)

    if course_name not in df["course_title"].values:
        return pd.DataFrame()

    idx = df[df["course_title"] == course_name].index[0]

    similarity_scores = list(enumerate(similarity_matrix[idx]))

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_courses = []

    for course in similarity_scores:

        row = df.iloc[course[0]]

        recommended_courses.append({
            "Course Title": row["course_title"],
            "Category": row["category"],
            "Difficulty Level": row["difficulty_level"],
            "Rating": row["rating"],
            "Description": row["description"]
        })

    return pd.DataFrame(recommended_courses)