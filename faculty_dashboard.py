import streamlit as st

def faculty_dashboard():

    st.sidebar.title("Faculty Menu")

    menu = st.sidebar.selectbox(
        "Select Option",
        ["Dashboard", "Attendance", "Assignments", "Profile"]
    )

    if menu == "Dashboard":

        st.header("📊 Faculty Dashboard")

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Students", "60")
        col2.metric("Assignments Given", "8")
        col3.metric("Classes Taken", "20")

    elif menu == "Attendance":

        st.header("📅 Manage Attendance")

        st.write("Faculty can mark attendance here")

    elif menu == "Assignments":

        st.header("📚 Upload Assignment")

        st.file_uploader("Upload Assignment")

    elif menu == "Profile":

        st.header("👤 Profile")

        st.write("User:", st.session_state.user)
        st.write("Role: Faculty")
