import streamlit as st

# Create user dictionary
if "users" not in st.session_state:
    st.session_state.users = {}

# Main page
if "page" not in st.session_state:
    st.session_state.page = 'main'

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
    username = st.button("Username")
    password = st.button("Password", type="password")

    # Login logic
    if st.button("Login"):
        if username not in st.session_state.users:
            st.error("Username does not exist.")
        else:
            if st.session_state.users[username]["password"] == password:
                st.success("Login successful!")
            else:
                st.error("Incorrect password.")
    
    if st.button("Back"):
        st.sessoin_state.page = "main"

# Registration page
elif st.session_state.page == "register":
    st.title("Register")

    reg_username = st.text_input("Choose a username.")
    reg_password = st.text_input("Choose a password.", type="password")
    reg_email = st.text_input("Enter your email.")

    if st.button("Submit Registration"):
        if username in st.session_state.users:
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
        st.sessoin_state.page = "main"
        