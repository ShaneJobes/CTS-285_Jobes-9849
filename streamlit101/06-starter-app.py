# ═══════════════════════════════════════════════════════════════════════
#  CITIZEN WELLNESS PORTAL™
#  AlgoCratic Futures - ORANGE Clearance Authorization
# ═══════════════════════════════════════════════════════════════════════
#
#  Your mission: Build a login/registration system with dashboard
#  using Streamlit and AI-assisted learning.
#
#  This file is a STARTING POINT, not a solution. You will need to:
#  1. Learn Streamlit basics using LLM assistance
#  2. Implement the TODOs below
#  3. Document your learning process in PROCESS.md
#
#  Run with: streamlit run app.py
#
# ═══════════════════════════════════════════════════════════════════════

import streamlit as st

# ─────────────────────────────────────────────────────────────────────────
# PAGE CONFIGURATION
# This must be the first Streamlit command
# ─────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Citizen Wellness Portal™",
    page_icon="🏛️",
    layout="centered"
)

# ─────────────────────────────────────────────────────────────────────────
# SESSION STATE INITIALIZATION
# 
# TODO: Initialize your session state variables here
# 
# You'll need at minimum:
#   - A way to track if user is logged in (boolean)
#   - A place to store registered users (dict)
#   - The current user's username (string)
#
# Hint: Ask your LLM "How do I initialize session state in Streamlit 
#       so it doesn't reset on every interaction?"
# ─────────────────────────────────────────────────────────────────────────

# Example (you may need to modify):
# if 'some_variable' not in st.session_state:
#     st.session_state.some_variable = initial_value

pass  # Remove this when you add your initialization code


# ─────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS (Optional but recommended for organization)
# ─────────────────────────────────────────────────────────────────────────

def check_credentials(username: str, password: str) -> bool:
    """
    Verify if username and password match a registered user.
    
    TODO: Implement this function
    
    Returns:
        True if credentials are valid, False otherwise
    """
    pass  # Replace with your implementation


def register_user(username: str, password: str) -> tuple[bool, str]:
    """
    Register a new user.
    
    TODO: Implement this function
    
    Returns:
        Tuple of (success: bool, message: str)
        Example: (True, "Registration successful!")
        Example: (False, "Username already taken")
    """
    pass  # Replace with your implementation


def show_login_form():
    """
    Display the login form.
    
    TODO: Implement this function
    
    Should include:
    - Username input
    - Password input (hidden)
    - Submit button
    - Error messages for invalid credentials
    - Update session state on successful login
    
    Hint: Ask your LLM about st.form() to prevent reruns on every keystroke
    """
    st.header("🔐 Citizen Authentication Portal")
    
    # Your login form implementation here
    st.info("TODO: Implement login form")


def show_registration_form():
    """
    Display the registration form.
    
    TODO: Implement this function
    
    Should include:
    - Username input
    - Password input (hidden)
    - Validation (username not taken, password length)
    - Success/error messages
    """
    st.header("📝 New Citizen Registration")
    
    # Your registration form implementation here
    st.info("TODO: Implement registration form")


def show_dashboard():
    """
    Display the logged-in user's dashboard.
    
    TODO: Implement this function
    
    Should include:
    - Welcome message with username
    - Algorithmic Satisfaction Metrics (mock data is fine)
    - Logout button
    
    Hint: Look into st.metric() and st.columns() for nice layouts
    """
    st.title("🏛️ Citizen Wellness Portal™")
    
    # Your dashboard implementation here
    st.info("TODO: Implement dashboard")
    
    # Logout button (you'll need to implement the logic)
    if st.button("Logout"):
        st.info("TODO: Implement logout logic")


# ─────────────────────────────────────────────────────────────────────────
# MAIN APPLICATION LOGIC
# ─────────────────────────────────────────────────────────────────────────

def main():
    """
    Main application entry point.
    
    TODO: Implement the main flow
    
    Logic should be:
    - If user is logged in → show dashboard
    - If user is NOT logged in → show login/registration options
    
    Hint: You might use st.tabs() to switch between login and register,
          or use session state to track which "page" to show.
    """
    
    # ─────────────────────────────────────────────────────────────────────
    # TEMPORARY DEBUG INFO (remove before submission)
    # Uncomment these lines to see your session state while developing
    # ─────────────────────────────────────────────────────────────────────
    # with st.sidebar:
    #     st.write("🔧 Debug: Session State")
    #     st.write(dict(st.session_state))
    
    # ─────────────────────────────────────────────────────────────────────
    # YOUR MAIN LOGIC HERE
    # ─────────────────────────────────────────────────────────────────────
    
    st.title("🏛️ Citizen Wellness Portal™")
    st.caption("*The Algorithm welcomes you.*")
    
    st.warning("""
    **This is the starter template.** 
    
    Your tasks:
    1. Initialize session state variables above
    2. Implement the helper functions
    3. Add main logic to show login/register OR dashboard based on login status
    4. Document everything in PROCESS.md
    
    Start by asking your LLM: "Explain how Streamlit's execution model 
    differs from Flask. What happens when a user clicks a button?"
    """)
    
    # TODO: Replace the warning above with your actual implementation:
    # 
    # if st.session_state.get('logged_in', False):
    #     show_dashboard()
    # else:
    #     # Show login and registration options
    #     tab1, tab2 = st.tabs(["Login", "Register"])
    #     with tab1:
    #         show_login_form()
    #     with tab2:
    #         show_registration_form()


# ─────────────────────────────────────────────────────────────────────────
# RUN THE APP
# ─────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()


# ═══════════════════════════════════════════════════════════════════════
# LEARNING NOTES (Add your own notes here as you learn)
# ═══════════════════════════════════════════════════════════════════════
#
# Key Streamlit Concepts:
# - st.session_state: ...
# - st.form(): ...
# - st.rerun(): ...
#
# Things that surprised me:
# - ...
#
# Things that confused me:
# - ...
#
# ═══════════════════════════════════════════════════════════════════════
