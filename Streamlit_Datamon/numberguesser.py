import streamlit as st
import random

# --- Helper Functions ---

def get_difficulty_range(choice):
    """Return (min_val, max_val, impossible_mode) based on difficulty."""
    if choice == "Easy (0-10)":
        return 0, 10, False
    elif choice == "Medium (0-30)":
        return 0, 30, False
    elif choice == "Hard (0-100)":
        return 0, 100, False
    elif choice == "EXTREME (-500 to 500)":
        return -500, 500, False
    elif choice == "IMPOSSIBLE (Good luck, chump!)":
        return 0, 5, True
    return 0, 10, False


def generate_missing_number_problem(min_val, max_val, impossible=False):
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)

    if operation == '+':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a + b
    elif operation == '-':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a - b
    elif operation == '*':
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        result = a * b
    elif operation == '/':
        b = random.randint(1, max_val if max_val != 0 else 1)
        result = random.randint(min_val, max_val)
        a = b * result

    if impossible:
        problem = f"_ {operation} _ = _"
        correct_answer = (a, b, result)
    else:
        missing = random.choice(['left', 'right', 'result'])
        if missing == 'left':
            problem = f"_ {operation} {b} = {result}"
            correct_answer = a
        elif missing == 'right':
            problem = f"{a} {operation} _ = {result}"
            correct_answer = b
        else:
            problem = f"{a} {operation} {b} = _"
            correct_answer = result

    return problem, correct_answer


# --- Streamlit App ---

st.title("🔢 Missing Number Box Game")
st.write("Fill in the blank (_) to complete the equation. You have **3 lives**!")

# Initialize session state
if "fails" not in st.session_state:
    st.session_state.fails = 0
if "question_num" not in st.session_state:
    st.session_state.question_num = 1
if "problem" not in st.session_state:
    st.session_state.problem = None
if "correct_answer" not in st.session_state:
    st.session_state.correct_answer = None
if "impossible_mode" not in st.session_state:
    st.session_state.impossible_mode = False
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Difficulty selection
difficulty = st.selectbox(
    "Choose your difficulty:",
    [
        "Easy (0-10)",
        "Medium (0-30)",
        "Hard (0-100)",
        "EXTREME (-500 to 500)",
        "IMPOSSIBLE (Good luck, chump!)",
    ],
    key="difficulty",
)

# Start or restart
if st.button("🎮 Start / Next Problem"):
    min_val, max_val, impossible = get_difficulty_range(difficulty)
    st.session_state.problem, st.session_state.correct_answer = generate_missing_number_problem(
        min_val, max_val, impossible
    )
    st.session_state.impossible_mode = impossible
    st.session_state.question_num += 1
    st.session_state.feedback = ""

# Game content
if not st.session_state.game_over and st.session_state.problem:
    st.markdown(f"### Problem {st.session_state.question_num}: {st.session_state.problem}")

    if st.session_state.impossible_mode:
        user_input = st.text_input("Enter three numbers (e.g. 3,4,12):", key="input_impossible")
    else:
        user_input = st.text_input("Enter your answer:", key="input_normal")

    if st.button("Submit Answer"):
        if st.session_state.impossible_mode:
            cleaned = user_input.replace(",", " ").strip()
            parts = cleaned.split()
            if len(parts) != 3:
                st.warning("Enter three numbers separated by commas or spaces.")
            else:
                try:
                    user_answers = [float(p) if "." in p else int(p) for p in parts]
                    a_corr, b_corr, res_corr = st.session_state.correct_answer
                    correct = all(abs(u - c) < 0.001 for u, c in zip(user_answers, (a_corr, b_corr, res_corr)))
                    if correct:
                        st.success("✅ Correct!")
                    else:
                        st.error(f"❌ Incorrect. Correct answers: {a_corr}, {b_corr}, {res_corr}")
                        st.session_state.fails += 1
                except ValueError:
                    st.warning("Please enter valid numbers.")
        else:
            try:
                user_val = float(user_input) if "." in user_input else int(user_input)
                correct_val = st.session_state.correct_answer
                if abs(user_val - correct_val) < 0.001:
                    st.success("✅ Correct!")
                else:
                    st.error(f"❌ Incorrect. The correct answer was {correct_val}.")
                    st.session_state.fails += 1
            except ValueError:
                st.warning("Please enter a valid number.")

        # Check for game over
        if st.session_state.fails >= 3:
            st.session_state.game_over = True
            st.error("💀 Game Over! You reached 3 incorrect answers.")
        else:
            st.info(f"Lives remaining: {3 - st.session_state.fails}")

# Reset game
if st.session_state.game_over:
    if st.button("🔁 Play Again"):
        st.session_state.fails = 0
        st.session_state.question_num = 1
        st.session_state.problem = None
        st.session_state.correct_answer = None
        st.session_state.game_over = False
        st.experimental_rerun()