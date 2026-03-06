import streamlit as st
import pandas as pd
import plotly.express as px


def show_faculty_dashboard():

    st.title("👨‍🏫 Faculty Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Students", "120")
    col2.metric("Assignments Submitted", "85")
    col3.metric("Classes Today", "4")

    st.subheader("Student Performance")

    data = pd.DataFrame({
        "Student": ["A", "B", "C", "D"],
        "Marks": [80, 75, 90, 60]
    })

    fig = px.line(data, x="Student", y="Marks")
    st.plotly_chart(fig, use_container_width=True)
