import streamlit as st
st.set_page_config(
    page_title="Quiz",
    page_icon="🧠"
)
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
st.title("Welcome to my Quiz 🧠")
if st.button("Click here to continue"):
    st.switch_page("Quiz_pages/Difficulty.py")