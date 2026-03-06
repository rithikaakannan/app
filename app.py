import streamlit as st
from login import student_login, faculty_login
from student_dashboard import student_dashboard
from faculty_dashboard import faculty_dashboard

st.set_page_config(page_title="CLMS", layout="wide")

if "role" not in st.session_state:
    st.session_state.role = None

st.title("🎓 Centralized Learning Management System")

# LOGIN PAGE
if st.session_state.role is None:

    option = st.radio("Login As", ["Student", "Faculty"])

    if option == "Student":
        student_login()

    else:
        faculty_login()

# DASHBOARD PAGE
else:

    if st.session_state.role == "student":
        student_dashboard()

    if st.session_state.role == "faculty":
        faculty_dashboard()

    if st.sidebar.button("Logout"):
        st.session_state.role = None
        st.rerun()
