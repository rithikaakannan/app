import streamlit as st

def student_dashboard():

    st.sidebar.title("Student Menu")

    menu = st.sidebar.selectbox(
        "Select Option",
        ["Dashboard", "Attendance", "Assignments", "Profile"]
    )

    if menu == "Dashboard":

        st.header("📊 Student Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("Attendance", "85%")
        col2.metric("Assignments Submitted", "5")
        col3.metric("Pending Assignments", "2")

    elif menu == "Attendance":

        st.header("📅 Attendance")

        st.write("Your attendance is 85%")

    elif menu == "Assignments":

        st.header("📚 Assignments")

        st.write("1. AI Assignment")
        st.write("2. Python Lab")

    elif menu == "Profile":

        st.header("👤 Profile")

        st.write("User:", st.session_state.user)
        st.write("Role: Student")
