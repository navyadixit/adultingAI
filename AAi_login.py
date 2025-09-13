import streamlit as st
import sqlite3


#Configuring Streamlit page
st.set_page_config(
    page_title="AdultingAI Admin Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded")
# Custom CSS for better styling
st.markdown(""" <style>
.stApp{background-color: #f4c2c2  ;}
</style>""", unsafe_allow_html= True)
st.markdown("""
<style>
h2 {
    font-size: 2.5rem;
    font-weight: bold;
    color: #8e5151    ;
    text-align: center;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<style>
h1 {
    font-size: 2.25rem;        /* Larger size for title */
    font-weight: bold;
    color: #8e5151;         /* Your chosen color */
    text-align: justify;
    margin-bottom: 2rem;
}

p {
    font-size: 1.2rem;      /* Size for paragraphs (st.write content) */
    color: #333333;
    text-align: justify;    /* Or 'center' if preferred */
    margin-bottom: 1.5rem;
}
</style>
""",
unsafe_allow_html=True
)
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #8e5151;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #f4c2c2;
    }
    </style>
""", unsafe_allow_html=True)
connection = sqlite3.connect('AAi.db')
cur = connection.cursor()
cur.execute("SELECT Username, Password FROM Users")
users = cur.fetchall()  # [(username, password), ...]

st.title("Login")
login_form = st.form("login_form")
username_input = login_form.text_input("Username").strip()
password_input = login_form.text_input("Password", type="password").strip()
login_button = login_form.form_submit_button("Login")
cur.execute("SELECT Username, Password FROM Users")
users = cur.fetchall() 
if login_button:
    # ✅ FIX 2: Use len(users) instead of cur.rowcount
    for i in range(len(users)):
        if username_input == users[i][0] and password_input == users[i][1]:
            st.success("Login successful!")
            st.switch_page("pages/AAi_Mainpage.py")
            break
    else:
        st.error("Invalid username or password")

if st.button("signup"):
    st.switch_page("pages/AAi_signin.py")   




