import streamlit as st

st.set_page_config(page_title="CLMS Login", layout="centered")

# ---------- USERS ----------
students = {
    "student1": "123",
    "student2": "123"
}

faculty = {
    "faculty1": "123",
    "faculty2": "123"
}

# ---------- BACKGROUND + STYLE ----------
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
backdrop-filter: blur(15px);
width:350px;
margin:auto;
margin-top:120px;
text-align:center;
box-shadow:0px 0px 30px rgba(0,0,0,0.3);
}

.title{
font-size:30px;
color:white;
font-weight:bold;
margin-bottom:20px;
}

.stTextInput>div>div>input{
border-radius:10px;
}

.stButton>button{
width:100%;
border-radius:25px;
background-color:white;
color:black;
font-weight:bold;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------- LOGIN UI ----------
st.markdown('<div class="login-box">', unsafe_allow_html=True)
st.markdown('<div class="title">Login</div>', unsafe_allow_html=True)

login_type = st.selectbox("Login As", ["Student", "Faculty"])

user = st.text_input("User ID")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if login_type == "Student":
        if user in students and students[user] == password:
            st.success("Student Login Successful")
            st.session_state["role"] = "student"
        else:
            st.error("Invalid Student ID or Password")

    if login_type == "Faculty":
        if user in faculty and faculty[user] == password:
            st.success("Faculty Login Successful")
            st.session_state["role"] = "faculty"
        else:
            st.error("Invalid Faculty ID or Password")

st.markdown('</div>', unsafe_allow_html=True)
