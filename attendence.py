import streamlit as st

def student_attendance():

    st.header("📅 Student Attendance")

    st.write("Your Attendance Percentage: **85%**")

    data = {
        "Subject": ["AI", "Python", "DBMS"],
        "Attendance": ["90%", "80%", "85%"]
    }

    st.table(data)
