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
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is 12 × 8?",
        "options": ["86", "96", "108", "92"],
        "answer": "96"
    },
    {
        "question": "Which gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": "Carbon dioxide"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "Which is the largest planet in our Solar System?",
        "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": ["50°C", "75°C", "100°C", "150°C"],
        "answer": "100°C"
    },
    {
        "question": "Which part of a plant carries out most photosynthesis?",
        "options": ["Root", "Stem", "Leaf", "Flower"],
        "answer": "Leaf"
    },
    {
        "question": "What is the square of 15?",
        "options": ["125", "200", "225", "250"],
        "answer": "225"
    },
    {
        "question": "Which organ pumps blood around the human body?",
        "options": ["Lungs", "Brain", "Heart", "Kidney"],
        "answer": "Heart"
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
