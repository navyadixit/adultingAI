import google.generativeai as genai
import streamlit as st
import sqlite3
genai.configure(api_key='AIzaSyDiDshd1hSTki5ZQc5es4rcMFkGIw44ZKY')
model=genai.GenerativeModel("gemini-1.5-flash")
import sqlite3
st.title("Finance")
if st.button("Main page"):
    st.switch_page("d:\python312\pages\AAi_Mainpage.py")
# assume you already have username, age, income_type, income_amount, savings_goal, necessities, gmail, dietary_pref variables
username = st.text_input("Username")
age = st.number_input("Age", min_value=10, max_value=100, value=18)
income_type = st.radio("Income type", ("Salary", "Pocket Money"))
income_amount = st.number_input("Monthly income (INR)", min_value=0)
savings_goal = st.number_input("Monthly savings target (INR)", min_value=0)
necessities = st.text_area("Necessities to buy (comma separated)")
gmail = st.text_input("Email (optional)")
dietary_pref = st.selectbox("Dietary preference", ("No preference","Vegetarian","Vegan","Other"))

if st.button("Generate advice prompt"):
    prompt = f"""
You are a friendly, practical personal finance coach. Use the user's details below to give concise, realistic, and actionable financial advice tailored to their situation. Use simple language and include a 1-month plan with steps they can follow.

User profile:
- Username: {username}
- Age: {age}
- Income type: {income_type}
- Monthly income (INR): {income_amount}
- Monthly savings target (INR): {savings_goal}
- Necessities they want to buy: {necessities}
- Email: {gmail}
- Dietary preference: {dietary_pref}

Tasks:
1. Quickly assess whether the savings target is realistic for their income. Show the savings target as a % of income.
2. Give a recommended monthly budget split (essentials / savings / discretionary) and explain why, adapting classic rules (e.g., 50/30/20) to the user's numbers.
3. Offer 5 practical, prioritized actions the user can do this month to reach their savings goal (specific, measurable, and low-effort steps).
4. If the user lists a necessity to buy that is large ( > 20% of monthly income ), recommend whether to: buy now, delay, or plan a small-savings buffer + timeline.
5. Suggest 3 low-cost alternatives for common necessities (e.g., cheaper groceries, cheaper transport, peer-sourced items).
6. End with a two-line motivational message and one quick habit the user can start today.

Tone: encouraging, non-judgemental, simple. If any input is missing or unclear, ask exactly one clear follow-up question.
"""
    response=model.generate_content(prompt)
    st.write(response.text)
