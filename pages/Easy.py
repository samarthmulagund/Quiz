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
        "question": "Q1. What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Q2. Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Q3. What is 12 × 8?",
        "options": ["86", "96", "108", "92"],
        "answer": "96"
    },
    {
        "question": "Q4. Which gas do plants absorb during photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": "Carbon dioxide"
    },
    {
        "question": "Q5. How many sides does a hexagon have?",
        "options": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "Q6. Which is the largest planet in our Solar System?",
        "options": ["Earth", "Saturn", "Jupiter", "Neptune"],
        "answer": "Jupiter"
    },
    {
        "question": "Q7. What is the boiling point of water at sea level?",
        "options": ["50°C", "75°C", "100°C", "150°C"],
        "answer": "100°C"
    },
    {
        "question": "Q8. Which part of a plant carries out most photosynthesis?",
        "options": ["Root", "Stem", "Leaf", "Flower"],
        "answer": "Leaf"
    },
    {
        "question": "Q9. What is the square of 15?",
        "options": ["125", "200", "225", "250"],
        "answer": "225"
    },
    {
        "question": "Q10. Which organ pumps blood around the human body?",
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
col1, col2, col3, col4= st.columns(4)
with col1:
    if st.button("Check Answer", key="check_answer"):
        if answer == q["answer"]:
            if not st.session_state.answered:
                st.session_state.score = st.session_state.score + 1
                st.success("Correct!")

        else:
            st.error("Wrong!, The corrct answer is ", q["answer"])

    st.session_state.answered = True
i = 0
with col2:
    if st.button("Next Question"):
        if st.session_state.question_number < len(questions) - 1:
            st.session_state.question_number += 1
            st.session_state.answered = False
            st.rerun()
with col4:
    if st.session_state.question_number == len(questions)-1:
        if st.button("Finished"):
            st.switch_page("pages/Final Score.py")
with col3:
    if st.button("Skip"):
        if st.session_state.question_number < len(questions) - 1:
            st.session_state.question_number = st.session_state.question_number + 2
            st.session_state.answered = False
            st.rerun()
score_display.write(f"🏆 Score: {st.session_state.score}")
