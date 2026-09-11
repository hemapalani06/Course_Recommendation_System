import streamlit as st
import pandas as pd
from recommend import load_data, preprocess_data, build_model, recommend


st.set_page_config(page_title="Course Recommender", layout="wide")


st.markdown("""
<style>
body {
    background-color: #f0f8ff;
}

.stApp {
    background-color: #f0f8ff;
}

h1 {
    color: #ff4b4b;
    text-align: center;
}

.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.title("Course Recommendation System")


uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    df = preprocess_data(df)
    similarity = build_model(df)

    course_list = df["course_title"].unique()
    selected_course = st.selectbox("Select Course", course_list)

    if st.button("Recommend"):

        result = recommend(selected_course, df, similarity)

        if result.empty:
            st.warning("No recommendations found")
        else:
            st.subheader("Recommended Courses")

            for _, row in result.iterrows():
                st.markdown(f"""
                ### {row['Course Title']}
                - **Category:** {row['Category']}
                - **Difficulty:** {row['Difficulty Level']}
                - **Rating:** {row['Rating']}
                - **Description:** {row['Description']}
                ---
                """)
else:
    st.info("Please upload a CSV file")