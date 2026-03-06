import streamlit as st

from login import student_login, faculty_login

from dashboard.student_dashboard import student_dashboard
from dashboard.faculty_dashboard import faculty_dashboard

from attendance.student_attendance import student_attendance
from attendance.faculty_attendance import faculty_attendance

from assignments.student_assignments import student_assignments
from assignments.faculty_assignments import faculty_assignments

st.set_page_config(page_title="CLMS", layout="wide")

if "role" not in st.session_state:
    st.session_state.role = None

st.title("🎓 Centralized Learning Management System")

# LOGIN
if st.session_state.role is None:

    option = st.radio("Login As", ["Student", "Faculty"])

    if option == "Student":
        student_login()

    else:
        faculty_login()

# DASHBOARD
else:

    menu = st.sidebar.selectbox(
        "Menu",
        ["Dashboard", "Attendance", "Assignments", "Logout"]
    )

    if menu == "Dashboard":

        if st.session_state.role == "student":
            student_dashboard()

        else:
            faculty_dashboard()

    elif menu == "Attendance":

        if st.session_state.role == "student":
            student_attendance()

        else:
            faculty_attendance()

    elif menu == "Assignments":

        if st.session_state.role == "student":
            student_assignments()

        else:
            faculty_assignments()

    elif menu == "Logout":

        st.session_state.role = None
        st.rerun()
