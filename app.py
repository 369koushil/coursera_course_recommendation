import streamlit as st
import pandas as pd

df = pd.read_pickle("courses_df.pkl")

st.set_page_config(page_title="Course Recommender", layout="wide")
st.title("📘 Coursera Course Recommendation System")

course_selected = st.selectbox(
    "Select a course to get similar recommendations:",
    df['title'],
    index=0,
    placeholder="Choose a course",
)

if st.button("🔎 Get Similar Courses"):
    matched_row = df[df['title'] == course_selected]

    if not matched_row.empty:
        recommended_titles = matched_row.iloc[0]['recommended_courses']
        st.subheader("🔁 Top 5 Recommended Courses:")
        cols = st.columns(2)

        for i, course_title in enumerate(recommended_titles):
            course_row = df[df['title'] == course_title]

            if not course_row.empty:
                course = course_row.iloc[0]

                instructor = course.get('Instructor', 'N/A')
                rating = course.get('rating', 'N/A')
                org = course.get('Organization', 'N/A')
                url = course.get('URL', '#')

                with cols[i % 2]:
                    st.markdown(f"""
                    <div style="border: 1px solid #333; border-radius: 10px; padding: 16px; margin-bottom: 16px; background-color: #1e1e1e; color: white;">
                        <h4 style="margin-bottom: 5px;">📘 {course['title']}</h4>
                        <p>👨‍🏫 <strong>Instructor:</strong> {instructor}</p>
                        <p>🏢 <strong>Organization:</strong> {org}</p>
                        <p>⭐ <strong>Rating:</strong> {rating}</p>
                        <a href="{url}" target="_blank" style="text-decoration: none;">
                            <button style="background-color: #4CAF50; color: white; border: none; padding: 8px 12px; border-radius: 5px; cursor: pointer;">
                                🔗 View Course
                            </button>
                        </a>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning(f"Course details not found for: {course_title}")
    else:
        st.error("Course not found in dataset.")