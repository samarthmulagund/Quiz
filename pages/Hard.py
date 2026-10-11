import streamlit as st
import base64
if "answered" not in st.session_state:
    st.session_state.answered = False
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_number" not in st.session_state:
    st.session_state.question_number = 0

st.set_page_config(
    page_title="Quiz",
    page_icon="🧠"
)
st.title("🧠 My Quiz")




score_display = st.empty()


questions = [
    {
        "question": "Q1. Which is the largest desert in the world?",
        "options": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctic Desert"],
        "answer": "Antarctic Desert"
    },
    {
        "question": "Q2. Who was the first Indian to win a Nobel Prize?",
        "options": ["Rabindranath Tagore", "C.V Raman", "Amartya Sen", "Mother Teresa"],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "Q3. Which planet has the largest number of moons currently known?",
        "options": ["Saturn", "Neptune", "Uranus", "Earth"],
        "answer": "Saturn"
    },
    {
        "question": "Q4. Which Indian state has the longest coastline?",
        "options": ["Karnataka", "Maharashtra", "Gujarat", "Kerala"],
        "answer": "Gujarat"
    },
    {
        "question": "Q5. What is the chemical symbol for tungsten?",
        "options": ["T", "Tu", "W", "S"],
        "answer": "W"
    },
    {
        "question": "Q6. Which is the deepest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Southern Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Q7. Who founded the Maurya Empire?",
        "options": ["Ashoka", "Chandragupta Maurya", "Akbar", "Bindusara"],
        "answer": "Chandragupta Maurya"
    },
    {
        "question": "Q8. Which instrument is used to measure atmospheric pressure?",
        "options": ["Hygrometer", "Anemometer", "Seismometer", "Barometer"],
        "answer": "Barometer"
    },
    {
        "question": "Q9. Which country is known as the “Land of the Rising Sun”",
        "options": ["India", "China", "USA", "Japan"],
        "answer": "Japan"
    },
    {
        "question": "Q10. Which is the only continent through which all lines of longitude pass?",
        "options": ["Africa", "Asia", "Australia", "Europe"],
        "answer": "Africa"
    }
]
q = questions[st.session_state.question_number]
st.write(
    f"Question {st.session_state.question_number + 1} of {len(questions)}"
)

st.write(q["question"])

answer = st.radio(
    "Choose your answer:",
    q["options"],
    key = f"question_{st.session_state.question_number}"
)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("Check Answer", key="check_answer"):
        if answer == q["answer"]:
            if not st.session_state.answered:
                st.session_state.score = st.session_state.score + 1
                st.success("Correct!")

        else:
            st.error("Wrong!, The correct answer is ", q["answer"])

        st.session_state.answered = True
i = 0
with col2:
    if st.button("Next Question"):
        if st.session_state.question_number < len(questions) - 1:
            st.session_state.question_number += 1
            st.session_state.answered = False
            st.rerun()

with col5:
    if st.session_state.question_number == len(questions)-1:
        if st.button("Finished"):
            st.switch_page("pages/Final Score.py")
with col4:
    if st.button("Skip"):
        if st.session_state.question_number < len(questions) - 1:
            st.session_state.question_number = st.session_state.question_number + 2
            st.session_state.answered = False
            st.rerun()
with col3:
    if st.session_state.question_number < len(questions) - 1:
        st.session_state.question_number = st.session_state.question_number - 1
        st.session_state.answered = False
        st.rerun()
score_display.write(f"🏆 Score: {st.session_state.score}")
