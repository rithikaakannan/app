import streamlit as st
import pandas as pd


def faculty_assignments():

    st.title("📂 Upload Assignment")

    title = st.text_input("Assignment Title")

    file = st.file_uploader("Upload File")

    if st.button("Upload"):
        st.success("Assignment Uploaded")


def student_assignments():

    st.title("📝 Assignments")

    data = pd.DataFrame({
        "Assignment": ["AI Project", "Python Lab"],
        "Due Date": ["10 Apr", "15 Apr"]
    })

    st.table(data)
