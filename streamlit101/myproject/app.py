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
    st.title ("welcome!")
    st.write("Please choose an option:")

    if st.button("Login"):
        st.session_state.page = "login"
    if st.button("Register"):
        st.session_state.page = "register"

# Login page
elif st.session_state.page == "login":
    st.title ("Login")


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
                "email" : reg_email
            }
            st.success("Registration Successful!")


    if st.button("Back"):
        st.session_state.page = "main"

elif st.session_state.page == "calculator":
    st.title("Calculator")

    # Display uses a DIFFERENT key so we can modify calc_display freely
    st.text_input("Display", value=st.session_state.calc_display, disabled=True)

    buttons = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["C", "0", "="],
    ]

    operator_buttons = ["+", "-", "*", "/"]

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

        # After changing the value, push it to the display widget
        st.session_state.display_box = st.session_state.calc_display

    # Number buttons
    for r, row in enumerate(buttons):
        cols = st.columns(3)
        for c, label in enumerate(row):
            if cols[c].button(label, key=f"btn_{r}_{c}_{label}"):
                pressButton(label)

    st.write("### Operators")

    # Operator buttons
    op_cols = st.columns(4)
    for i, op in enumerate(operator_buttons):
        if op_cols[i].button(op, key=f"op_btn_{i}_{op}"):
            pressButton(op)

    # Logout button
    if st.button("Logout", key="logout_btn"):
        st.session_state.page = "main"
        st.session_state.calc_display = "0"