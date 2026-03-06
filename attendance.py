import streamlit as st
import pandas as pd
def faculty_attendance():

    st.header("📅 Mark Attendance")

    students = ["Student1", "Student2", "Student3"]

    for student in students:
        st.checkbox(student)

    if st.button("Submit Attendance"):
        st.success("Attendance Recorded Successfully")
def student_attendance():

    st.header("📅 Student Attendance")

    st.write("Your Attendance Percentage: **85%**")

    data = {
        "Subject": ["AI", "Python", "DBMS"],
        "Attendance": ["90%", "80%", "85%"]
    }

    st.table(data)
