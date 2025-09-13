import streamlit as st
import google.generativeai as genai

st.title("Cooking AI")
genai.configure(api_key='AIzaSyDiDshd1hSTki5ZQc5es4rcMFkGIw44ZKY')
model=genai.GenerativeModel("gemini-1.5-flash")
if st.button("Main page"):
    st.switch_page("d:\python312\pages\AAi_Mainpage.py")
# Collect user inputs
username = st.text_input("Username")
age = st.number_input("Age", min_value=10, max_value=100, value=18)
diet_pref = st.radio("Dietary preference", ("Vegetarian", "Non-Vegetarian", "Vegan", "Other"))
groceries = st.text_area("Groceries you currently have (comma separated)")
skills = st.text_area("Cooking skills you want to learn (e.g., chopping, baking, meal prep)")
time_available = st.number_input("How much time do you usually have for cooking (minutes)?", min_value=0)
budget = st.number_input("Monthly food budget (INR)", min_value=0)

# Generate cooking advice prompt
if st.button("Generate Cooking Prompt"):
    prompt = f"""
You are a friendly and practical cooking mentor. Use the user's details below to give personalized cooking advice, recipes, and grocery tips.

User profile:
- Username: {username}
- Age: {age}
- Dietary preference: {diet_pref}
- Groceries they currently have: {groceries}
- Cooking skills they want to learn: {skills}
- Time usually available for cooking: {time_available} minutes
- Monthly food budget (INR): {budget}

Tasks:
1. Suggest 3 simple recipes they can cook with their current groceries (include quick instructions).
2. Recommend a weekly meal plan that matches their dietary preference, time, and budget.
3. Give 3 tips to save money while grocery shopping.
4. Provide 2 practical cooking techniques to improve their skills.
5. End with 1 motivational cooking tip (fun, encouraging, easy to try today).
"""
    response=model.generate_content(prompt)
    st.write(response.text)

