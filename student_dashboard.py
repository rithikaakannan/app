import streamlit as st
import pandas as pd
import plotly.express as px


def show_student_dashboard():

    st.title("🎓 Student Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Attendance", "85%")
    col2.metric("Assignments Pending", "2")
    col3.metric("Course Progress", "70%")

    st.subheader("Course Progress")

    data = pd.DataFrame({
        "Course": ["Python", "DSA", "DBMS", "AI"],
        "Progress": [80, 60, 75, 50]
    })

    fig = px.bar(data, x="Course", y="Progress", color="Course")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Notifications")

    st.info("Assignment 2 due tomorrow")
    st.info("AI class rescheduled")
