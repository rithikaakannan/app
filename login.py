import streamlit as st

# USERS
students = {
    "student1": "123",
    "student2": "123"
}

faculty = {
    "faculty1": "123",
    "faculty2": "123"
}

# ---------- STYLE ----------
def login_style():

    page_bg = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1501785888041-af3ef285b470");
    background-size: cover;
    background-position: center;
    }

    .login-box{
    background: rgba(255,255,255,0.1);
    padding:40px;
    border-radius:20px;
    backdrop-filter: blur(12px);
    width:380px;
    margin:auto;
    margin-top:120px;
    text-align:center;
    box-shadow:0px 0px 25px rgba(0,0,0,0.3);
    }

    .title{
    font-size:32px;
    color:white;
    font-weight:bold;
    margin-bottom:10px;
    }

    .stButton button{
    width:100%;
    border-radius:25px;
    background-color:white;
    color:black;
    font-weight:bold;
    }
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)


# ---------- STUDENT LOGIN ----------
def student_login():

    login_style()

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Student Login</div>', unsafe_allow_html=True)

    user = st.text_input("Student ID")
    password = st.text_input("Password", type="password")

    if st.button("Login as Student"):
        if user in students and students[user] == password:
            st.session_state["role"] = "student"
            st.session_state["user"] = user
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid ID or Password")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- FACULTY LOGIN ----------
def faculty_login():

    login_style()

    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    st.markdown('<div class="title">Faculty Login</div>', unsafe_allow_html=True)

    user = st.text_input("Faculty ID")
    password = st.text_input("Password", type="password")

    if st.button("Login as Faculty"):
        if user in faculty and faculty[user] == password:
            st.session_state["role"] = "faculty"
            st.session_state["user"] = user
            st.success("Login Successful")
            st.rerun()
        else:
            st.error("Invalid ID or Password")

    st.markdown('</div>', unsafe_allow_html=True)
