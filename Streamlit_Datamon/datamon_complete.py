import streamlit as st
import answerchecker
import missingnumber
import numberguesser
import memorybank

# --- Initialize Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- App Navigation Logic ---
if st.session_state.page == "home":
    st.title("🎮 Datamon’s Game Hub")
    st.write("Welcome! Choose a game to play below 👇")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧠 Equation Answer Checker"):
            st.session_state.page = "equation_checker"
        if st.button("🔢 Missing Number Box"):
            st.session_state.page = "missing_number"
    with col2:
        if st.button("🎯 Number Guesser"):
            st.session_state.page = "number_guesser"
        if st.button("⭐ Memory Bank Game"):
            st.session_state.page = "memory_bank"

elif st.session_state.page == "equation_checker":
    answerchecker.run_game()

elif st.session_state.page == "missing_number":
    missingnumber.run_game()

elif st.session_state.page == "number_guesser":
    numberguesser.run_game()

elif st.session_state.page == "memory_bank":
    memorybank.run_game()