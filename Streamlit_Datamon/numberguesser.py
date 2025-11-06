import streamlit as st
import random

def run_game():
    st.title("🧠 Number Guesser")

    # Back button
    if st.button("⬅️ Back to Main Menu"):
        st.session_state.page = "home"
        st.rerun()

    # Initialize session state variables
    if "game_running" not in st.session_state:
        st.session_state.game_running = False
    if "rand_num" not in st.session_state:
        st.session_state.rand_num = None
    if "rand_range" not in st.session_state:
        st.session_state.rand_range = 50
    if "wins" not in st.session_state:
        st.session_state.wins = 0
    if "total_guesses" not in st.session_state:
        st.session_state.total_guesses = 0
    if "round_guesses" not in st.session_state:
        st.session_state.round_guesses = 0
    if "message" not in st.session_state:
        st.session_state.message = ""

    st.title("🎯 Datamon Number Guesser")
    st.write("Welcome to the Number Guesser! Try to find the hidden number.")

    # --- Start or Quit Game ---
    if not st.session_state.game_running:
        if st.button("Start Game"):
            st.session_state.game_running = True
            st.session_state.rand_num = int(random.random() * 100)
            st.session_state.rand_range = 50
            st.session_state.round_guesses = 0
            st.session_state.message = ""
    else:
        if st.button("Quit Game"):
            st.session_state.game_running = False
            st.session_state.message = "Game ended. Thanks for playing!"

    # --- Game Active Section ---
    if st.session_state.game_running:
        st.write("### Current Round")
        min_range = (st.session_state.rand_num - st.session_state.rand_range) - int(random.random() * 5)
        max_range = (st.session_state.rand_num + st.session_state.rand_range) + int(random.random() * 5)
        st.write(f"The number is between **{min_range}** and **{max_range}**")

        guess_input = st.text_input("Enter your guess:")

        if st.button("Submit Guess"):
            # Validate input
            if not guess_input.strip():
                st.session_state.message = "Please enter a number before submitting."
                st.stop()

            try:
                guess = int(guess_input)
            except ValueError:
                st.session_state.message = "Invalid input! Please enter a valid integer."
                st.stop()

            st.session_state.total_guesses += 1
            st.session_state.round_guesses += 1

            if guess == st.session_state.rand_num:
                st.session_state.wins += 1
                st.session_state.message = f"✅ Correct! You found the number in {st.session_state.round_guesses} guesses!"
                st.session_state.game_running = False
            else:
                st.session_state.message = "❌ Wrong guess!"
                if st.session_state.rand_range >= 20:
                    st.session_state.rand_range -= 10

    # --- Display messages & stats ---
    if st.session_state.message:
        st.write(st.session_state.message)

    if not st.session_state.game_running and st.session_state.wins + st.session_state.total_guesses > 0:
        st.write("---")
        st.write("### 🏁 Game Stats")
        st.write(f"Wins: {st.session_state.wins}")
        st.write(f"Total Guesses: {st.session_state.total_guesses}")