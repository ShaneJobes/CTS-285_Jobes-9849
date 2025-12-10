import streamlit as st

# Create user dictionary
if "users" not in st.session_state:
    st.session_state.users = {}

# Main page
if "page" not in st.session_state:
    st.session_state.page = 'main'

if "calc_display" not in st.session_state:
    st.session_state.calc_display = "0"

if st.session_state.page == 'main':
    st.title("Welcome!")
    st.write("Please choose an option:")

    if st.button("Login"):
        st.session_state.page = "login"
    if st.button("Register"):
        st.session_state.page = "register"

# Login page
elif st.session_state.page == "login":
    st.title("Login")

    # Username and password input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login logic
    if st.button("Login"):
        if username not in st.session_state.users:
            st.error("Username does not exist.")
        else:
            if st.session_state.users[username]["password"] == password:
                st.success("Login successful!")
                st.session_state.page = "calculator"
            else:
                st.error("Incorrect password.")
    
    if st.button("Back"):
        st.session_state.page = "main"

# Registration page
elif st.session_state.page == "register":
    st.title("Register")

    reg_username = st.text_input("Choose a username.")
    reg_password = st.text_input("Choose a password.", type="password")
    reg_email = st.text_input("Enter your email.")

    if st.button("Submit Registration"):
        if reg_username in st.session_state.users:
            st.error("Username already exists")
        elif not reg_username or not reg_password or not reg_email:
            st.error("All fields must be filled out.")
        else:
            st.session_state.users[reg_username] = {
                "password": reg_password,
                "email": reg_email
            }
            st.success("Registration Successful!")
    
    if st.button("Login"):
        st.session_state.page = "login"

    if st.button("Back"):
        st.session_state.page = "main"

# ------------------------------
# CALCULATOR PAGE
# ------------------------------
elif st.session_state.page == "calculator":
    st.title("Calculator")

    # -------------------------------
    # 1. PROCESS BUTTON CLICKS FIRST
    # -------------------------------
    def pressButton(value):
        if value == "C":
            st.session_state.calc_display = "0"
        elif value == "=":
            try:
                st.session_state.calc_display = str(eval(st.session_state.calc_display))
            except:
                st.session_state.calc_display = "ERROR"
        else:
            if st.session_state.calc_display in ["0", "ERROR"]:
                st.session_state.calc_display = value
            else:
                st.session_state.calc_display += value

    # Hidden triggers for clicks
    for r, row in enumerate([
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["C", "0", "="],
    ]):
        for c, label in enumerate(row):
            if st.session_state.get(f"btn_trigger_{r}_{c}", False):
                pressButton(label)
                st.session_state[f"btn_trigger_{r}_{c}"] = False

    for i, op in enumerate(["+", "-", "*", "/"]):
        if st.session_state.get(f"op_trigger_{i}", False):
            pressButton(op)
            st.session_state[f"op_trigger_{i}"] = False

    # -------------------------------
    # 2. DRAW THE DISPLAY AFTER LOGIC
    # -------------------------------
    st.text_input("Display", value=st.session_state.calc_display, disabled=True)

    # -------------------------------
    # 3. DRAW BUTTON GRID
    # -------------------------------
    buttons = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["C", "0", "="],
    ]

    for r, row in enumerate(buttons):
        cols = st.columns(3)
        for c, label in enumerate(row):
            if cols[c].button(label, key=f"btn_{r}_{c}"):
                st.session_state[f"btn_trigger_{r}_{c}"] = True
                st.rerun()

    operator_buttons = ["+", "-", "*", "/"]

    op_cols = st.columns(4)

    for i, op in enumerate(operator_buttons):
        safe_label = f"\\{op}"  # escape markdown so it displays properly
        if op_cols[i].button(safe_label, key=f"op_btn_{i}_{op}"):
            pressButton(op)
            st.rerun()

    if st.button("Logout", key="logout_btn"):
        st.session_state.page = "main"
        st.session_state.calc_display = "0"
        st.rerun()