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
st.title("Choose the difficulty of your quiz 🧠")
if st.button("Easy"):
    st.switch_page("pages/Easy.py")

elif st.button("Medium"):
    st.switch_page("pages/Hard.py")