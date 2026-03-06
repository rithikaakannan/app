import streamlit as st
from streamlit_option_menu import option_menu

from login import student_login, faculty_login
from student_dashboard import show_student_dashboard
from faculty_dashboard import show_faculty_dashboard
from attendance import faculty_attendance, student_attendance
from assignments import faculty_assignments, student_assignments

st.set_page_config(page_title="CLMS", layout="wide")

# SESSION STATE
if "role" not in st.session_state:
    st.session_state["role"] = None


# ---------- LOGIN PAGE ----------
if st.session_state["role"] is None:

    st.title("🎓 Centralized Learning Management System")

    role = st.radio("Login As", ["Student", "Faculty"])

    if role == "Student":
        student_login()

    else:
        faculty_login()


# ---------- AFTER LOGIN ----------
else:

    with st.sidebar:

        selected = option_menu(
            "CLMS Menu",
            ["Home", "Dashboard", "Attendance", "Assignments", "Announcements", "Profile", "Logout"],
            icons=["house", "speedometer", "calendar", "book", "megaphone", "person", "box-arrow-right"],
            menu_icon="menu-button",
            default_index=0
        )

    if selected == "Home":
        st.title("🏫 Welcome to CLMS")
        st.write("Welcome:", st.session_state["user"])


    elif selected == "Dashboard":

        if st.session_state["role"] == "student":
            show_student_dashboard()
        else:
            show_faculty_dashboard()


    elif selected == "Attendance":

        if st.session_state["role"] == "student":
            student_attendance()
        else:
            faculty_attendance()


    elif selected == "Assignments":

        if st.session_state["role"] == "student":
            student_assignments()
        else:
            faculty_assignments()


    elif selected == "Announcements":
        st.title("📢 Announcements")
        st.info("Mid semester exams start next week")


    elif selected == "Profile":
        st.title("👤 Profile")
        st.write("User:", st.session_state["user"])
        st.write("Role:", st.session_state["role"])


    elif selected == "Logout":
        st.session_state["role"] = None
        st.rerun()
