import streamlit as st
import pandas as pd


def faculty_assignments():
import streamlit as st

def faculty_assignments():

    st.header("📚 Upload Assignment")

    title = st.text_input("Assignment Title")

    file = st.file_uploader("Upload File")

    if st.button("Publish Assignment"):
        st.success("Assignment Published")

def student_assignments():
    st.header("📚 Assignments")

    st.write("1. AI Assignment - Due Tomorrow")
    st.write("2. Python Lab - Due Friday")

    file = st.file_uploader("Upload Assignment")

    if file:
        st.success("Assignment Uploaded")
