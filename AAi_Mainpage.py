import streamlit as st
st.set_page_config(
    page_title="AdultingAI Admin Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded")
if st.button("Home page"):
    st.switch_page("d:\python312\AdultingAi.py")
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
st.header("AdultingAi")
col1, col2, col3 = st.columns([4,4,4])

with col1:
    if st.button("Finance"):
        st.switch_page("D:\python312\pages\AAi_finance.py")

with col3:
    if st.button("Cooking"):
        st.switch_page("D:\python312\pages\AAi_cooking.py")
