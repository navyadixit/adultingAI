import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import mysql.connector as mc
import json
from datetime import datetime, timedelta
import requests
import hashlib
import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

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

st.header("Welcome to AdultingAI")
st.title("About us")
st.write("We’ve all been there—standing in the grocery aisle, poking tomatoes and wondering if they're “ripe” or just “red” or staring at our bank balance, asking ourselves, “Where did my money go?” Adulting AI was born from those “Wait, why didn’t anyone teach me this?” moments.")

st.write("Designed for Gen Z, Adulting AI saves you from late-night Googling “how to cook rice” or whispering “what’s EMI?” in hushed tones. We’re here to turn life’s confusing little tasks into simple, fun lessons—because adulting doesn’t have to be a mystery.")

col1,col2,col3=st.columns([2,2,2])
with col1:
    st.write("Make sure you login for a better experience!")
    if st.button("LOGIN"):
         st.switch_page("D:\Python312\pages\AAi_login.py")
with col3:
    st.write("Make sure you sign in for amazing deals!")
    if st.button("SIGNIN"):
        st.switch_page("D:\Python312\pages\AAi_signin.py")
st.write("---")
st.title("Our Services")
st.write("""
--Personalized Finance Guidance

Bite-sized money tips

Budgeting challenges to build healthy habits

Gamified progress levels to track growth

Simplified financial terms for beginners

-- Cooking Made Easy

Grocery quality checker (how to spot fresh produce)

Quick and practical cooking tips

Recipe modules with veg/non-veg filters for easy access

-- Smart User Experience

Simple sign-up and login for accessibility

Clean, intuitive interface designed for ages 15–21

Engaging, interactive learning instead of boring lectures
""")


