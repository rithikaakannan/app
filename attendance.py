import streamlit as st
import pandas as pd


def faculty_attendance():

    st.title("📋 Mark Attendance")

    students = ["Student1", "Student2", "Student3"]

    attendance = {}

    for s in students:
        attendance[s] = st.checkbox(s)

    if st.button("Submit Attendance"):
        st.success("Attendance Saved")


def student_attendance():

    st.title("📊 My Attendance")

    data = pd.DataFrame({
        "Subject": ["Python", "DSA", "DBMS"],
        "Attendance %": [85, 78, 90]
    })

    st.table(data)
