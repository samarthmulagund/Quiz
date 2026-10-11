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
st.session_state.score = 0
score_display = st.empty()


questions = [
    {
        "question": "Which is the largest desert in the world?",
        "options": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctic Desert"],
        "answer": "Antarctic Desert"
    },
    {
        "question": "Who was the first Indian to win a Nobel Prize?",
        "options": ["Rabindranath Tagore", "C.V Raman", "Amartya Sen", "Mother Teresa"],
        "answer": "Rabindranath Tagore"
    },
    {
        "question": "Which planet has the largest number of moons currently known?",
        "options": ["Saturn", "Neptune", "Uranus", "Earth"],
        "answer": "Saturn"
    },
    {
        "question": "Which Indian state has the longest coastline?",
        "options": ["Karnataka", "Maharashtra", "Gujarat", "Kerala"],
        "answer": "Gujarat"
    },
    {
        "question": "What is the chemical symbol for tungsten?",
        "options": ["T", "Tu", "W", "S"],
        "answer": "W"
    },
    {
        "question": "Which is the deepest ocean in the world?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Southern Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Who founded the Maurya Empire?",
        "options": ["Ashoka", "Chandragupta Maurya", "Akbar", "Bindusara"],
        "answer": "Chandragupta Maurya"
    },
    {
        "question": "Which instrument is used to measure atmospheric pressure?",
        "options": ["Hygrometer", "Anemometer", "Seismometer", "Barometer"],
        "answer": "Barometer"
    },
    {
        "question": "Which country is known as the “Land of the Rising Sun”",
        "options": ["India", "China", "USA", "Japan"],
        "answer": "Japan"
    },
    {
        "question": "Which is the only continent through which all lines of longitude pass?",
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

if st.button("Check Answer", key="check_answer"):
    if answer == q["answer"]:
        if not st.session_state.answered:
            st.session_state.score = st.session_state.score + 1
            st.success("Correct!")

    else:
        st.error("Wrong!")

    st.session_state.answered = True
i = 0

if st.button("Next Question"):
    if st.session_state.question_number < len(questions) - 1:
        st.session_state.question_number += 1
        st.session_state.answered = False
        st.rerun()

if st.session_state.question_number == len(questions)-1:
    if st.button("Finished"):
        st.switch_page("Quiz_pages/Final Score.py")
score_display.write(f"🏆 Score: {st.session_state.score}")
