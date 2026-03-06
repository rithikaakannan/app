import streamlit as st

students = {
    "student1": "123",
    "student2": "123"
}

faculty = {
    "faculty1": "123",
    "faculty2": "123"
}

# STUDENT LOGIN
def student_login():

    st.subheader("Student Login")

    user = st.text_input("Student ID")
    password = st.text_input("Password", type="password")

    if st.button("Login as Student"):

        if user in students and students[user] == password:

            st.session_state.role = "student"
            st.session_state.user = user

            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid ID or Password")


# FACULTY LOGIN
def faculty_login():

    st.subheader("Faculty Login")

    user = st.text_input("Faculty ID")
    password = st.text_input("Password", type="password")

    if st.button("Login as Faculty"):

        if user in faculty and faculty[user] == password:

            st.session_state.role = "faculty"
            st.session_state.user = user

            st.success("Login Successful")
            st.rerun()

        else:
            st.error("Invalid ID or Password")
