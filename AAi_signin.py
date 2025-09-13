import streamlit as st
import sqlite3

# ---------- DB setup ----------
DB_PATH = "AAi.db"
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()

# Create table if not exists (matches your screenshot columns)
cur.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Username TEXT PRIMARY KEY,
    Password TEXT NOT NULL,
    name TEXT,
    age INTEGER,
    gmail TEXT,
    "dietery preference" TEXT
)
""")
conn.commit()

# ---------- Page config & simple styling ----------
st.set_page_config(page_title="Signup — AdultingAI", page_icon="🎓", layout="wide")
st.markdown(
    """<style>
    .stApp { background-color: #f4c2c2; }
    h1 { color: #8e5151; text-align: center; }
    div.stButton > button { background-color: #8e5151; color: white; border-radius: 8px; padding: 8px 20px; }
    </style>""",
    unsafe_allow_html=True
)

st.title("Create an Account")

# ---------- Signup form (single page) ----------
with st.form("signup_only_form"):
    username = st.text_input("Username").strip()
    password = st.text_input("Password", type="password").strip()
    confirm = st.text_input("Confirm Password", type="password").strip()
    full_name = st.text_input("Full name").strip()
    age = st.number_input("Age", min_value=1, max_value=120, value=18, step=1)
    gmail = st.text_input("Email (Gmail)").strip()
    diet = st.selectbox("Dietary preference", ["Vegetarian", "Vegan", "Non-Vegetarian", "Other"])
    submit = st.form_submit_button("Create Account")

if submit:
    # Basic validation
    if not username:
        st.error("Username is required.")
    elif not password:
        st.error("Password is required.")
    elif password != confirm:
        st.error("Passwords do not match.")
    elif not full_name:
        st.error("Full name is required.")
    elif not gmail:
        st.error("Email is required.")
    else:
        # Check username uniqueness
        cur.execute("SELECT 1 FROM Users WHERE Username = ?", (username,))
        if cur.fetchone():
            st.error("That username already exists. Pick a different one.")
        else:
            # Optional: prevent duplicate emails (uncomment if wanted)
            # cur.execute("SELECT 1 FROM Users WHERE gmail = ?", (gmail,))
            # if cur.fetchone():
            #     st.error("That email is already registered.")
            # else:
            try:
                cur.execute(
                    'INSERT INTO Users (Username, Password, name, age, gmail, "dietery preference") VALUES (?, ?, ?, ?, ?, ?)',
                    (username, password, full_name, int(age), gmail, diet)
                )
                conn.commit()
                
            except Exception as e:
                st.error("Error creating account: " + str(e))
            else:
                st.switch_page("D:\Python312\pages\AAi_Mainpage.py")

# Optional: show small debug (remove in production)
with st.expander("Admin: current users (debug)"):
    cur.execute("SELECT Username, name, age, gmail, \"dietery preference\" FROM Users")
    rows = cur.fetchall()
    st.write(rows)
