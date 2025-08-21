# 📘 Coursera Course Recommendation System
An interactive Streamlit application that recommends Coursera courses based on user selection, leveraging a pre-processed dataset.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [📘 Coursera Course Recommendation System](#-coursera-course-recommendation-system)

  - [Key Features](#key-features)

  - [Architecture Overview](#architecture-overview)

  - [Tech Stack](#tech-stack)

  - [Getting Started](#getting-started)

    - [Prerequisites](#prerequisites)

    - [Installation](#installation)

  - [Configuration](#configuration)

## Key Features

- Interactive web interface built with Streamlit.

- Allows users to select a Coursera course from a dropdown menu.

- Displays the top 5 most similar course recommendations.

- Provides detailed information for each recommended course, including Instructor, Organization, Rating, and a direct URL link.

- Utilizes a pre-processed dataset for efficient and fast recommendation retrieval.

## Architecture Overview
This project implements a straightforward course recommendation system. The core of the application is a single Streamlit script (`app.py`) that serves as the entire user interface. It operates by loading a pre-existing, pre-processed dataset (`courses_df.pkl`) which contains all the necessary course information and the pre-computed recommendations.

When a user interacts with the application by selecting a course, `app.py` directly queries this local `.pkl` file to fetch the corresponding list of recommended courses. The application then dynamically renders these results on the web page, providing a responsive and interactive experience without the need for a separate backend server or a real-time recommendation engine. The complex recommendation logic (e.g., similarity calculations) is assumed to have been performed offline during the generation of `courses_df.pkl`.

## Tech Stack

| Area | Tool | Version |
|---|---|---|
|---|---|---|
| Web Framework | Streamlit | ^1.x |
| Data Manipulation | Pandas | ^2.x |
|---|---|---|
| Numerical Operations | NumPy | ^1.x |
| Machine Learning (Implied) | Scikit-learn | ^1.x |
|---|---|---|
| File System Abstraction | fsspec | ^2023.x |
| Hugging Face Integration | huggingface_hub | ^0.x |
|---|---|---|



## Getting Started

### Prerequisites
Ensure you have Python 3.8 or higher installed on your system.

### Installation
1.  Clone the repository:

```bash
git clone https://github.com/369koushil/coursera_course_recommendation.git

cd coursera_course_recommendation

```
2.  Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv

source venv/bin/activate  # On Windows: `venv\Scripts\activate`

```
3.  Install the required Python packages:

```bash
pip install -r requirements.txt

```
4.  **Data File**: This application relies on a pre-processed data file named `courses_df.pkl`. This file is crucial for the application's functionality but is not included in this repository. You will need to generate this file by running a separate data processing script (which is not part of this repository's sample) that handles course data loading, similarity calculations, and recommendation pre-computation. Without `courses_df.pkl` in the project root, the application will not run successfully.

## Configuration
No specific environment variables are currently required for the basic operation of this application.

## Usage
To run the Streamlit application locally:

```bash
streamlit run app.py

```
After executing the command, the application will automatically open in your default web browser, typically at `http://localhost:8501`.

* *Interacting with the application
