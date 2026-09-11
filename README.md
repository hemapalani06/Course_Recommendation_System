# E-Learning Course Recommendation System

## Overview

* Developed a Python-based course recommendation application.
* Helps users discover relevant courses based on a selected course.
* Uses a content-based recommendation approach to identify similar courses.
* Provides an interactive web interface using Streamlit.

## Features

* Upload course data through a CSV file.
* Select a course from the available dataset.
* Generate relevant course recommendations.
* Display course title, category, difficulty level, rating, and description.
* Provides an interactive and user-friendly interface.

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* TF-IDF
* Cosine Similarity
* Jupyter Notebook

## Recommendation Method

* The system uses a **content-based recommendation approach**.
* Course information is processed to identify similarities between courses.
* **TF-IDF** is used to convert text-based course information into numerical features.
* **Cosine similarity** is used to measure the similarity between courses.
* The system recommends courses that are most relevant to the selected course.

## Dataset

* The project uses a dataset containing **3,500+ courses**.
* The dataset includes:

  * Course Title
  * Category
  * Difficulty Level
  * Rating
  * Description
  * Skills

## Application Workflow

* Upload the course dataset in CSV format.
* Select a course from the dropdown menu.
* Click the **Recommend** button.
* The system processes the selected course.
* Relevant courses are displayed with their details.

## Project Structure

```text
E-Learning-Course-Recommendation-System/
│
├── app.py
├── recommend.py
├── Coursera.csv
├── E_learning_recommended_system_project.ipynb
└── README.md
```

## File Description

* **app.py** – Contains the Streamlit application and user interface.
* **recommend.py** – Contains data preprocessing and recommendation logic.
* **Coursera.csv** – Contains the course dataset.
* **E_learning_recommended_system_project.ipynb** – Contains project development and experimentation.
* **README.md** – Contains project documentation.

#
## Run the Application

* Run the following command:

```bash
streamlit run app.py
```

* The application will open in your default web browser.

## Future Enhancements

* Add personalized recommendations based on user profiles.
* Add course filtering by category and difficulty level.
* Improve recommendation accuracy.
* Add rating-based recommendation ranking.
* Add user recommendation history.
* Deploy the application as a cloud-based web application.
