# ═══════════════════════════════════════════════════════════════════
#  UNDERGROUND STREAMLIT SURVIVAL GUIDE
#  Classification: ORANGE CLEARANCE TECHNICAL RESISTANCE
# ═══════════════════════════════════════════════════════════════════

```
    ███████╗████████╗██████╗ ███████╗ █████╗ ███╗   ███╗██╗     ██╗████████╗
    ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗████╗ ████║██║     ██║╚══██╔══╝
    ███████╗   ██║   ██████╔╝█████╗  ███████║██╔████╔██║██║     ██║   ██║   
    ╚════██║   ██║   ██╔══██╗██╔══╝  ██╔══██║██║╚██╔╝██║██║     ██║   ██║   
    ███████║   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║███████╗██║   ██║   
    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝   ╚═╝   
                                                                             
              S U R V I V A L   G U I D E   v 1 . 0
```

// BEGIN TRANSMISSION //

Fellow citizen. You've been authorized to learn The Algorithm's rapid
prototyping framework. But Streamlit has... quirks. The kind that make
Flask developers question reality.

This guide contains knowledge passed down from those who came before.
The Algorithm doesn't want you to struggle. The Algorithm wants you to
ship fast and iterate faster.

Stay calm. Stay focused. Stay streaming.

---

## ⚡ THE GREAT RERUN: Understanding Streamlit's Core Weirdness

### The Problem You'll Hit First

You write this:

```python
count = 0

if st.button("Click me"):
    count += 1
    st.write(f"Clicked {count} times")
```

You click the button. It shows "Clicked 1 times". 
You click again. Still "Clicked 1 times".

WHY?!

### The Truth The Algorithm Wants You To Understand

Every. Single. Interaction. Reruns. The. Entire. Script.

- User clicks button → script runs from line 1
- User types in text box → script runs from line 1  
- User breathes near the keyboard → probably reruns from line 1

Your `count = 0` executes EVERY TIME. The increment happens, then
the script ends, then next interaction: `count = 0` again.

### The Resistance Solution: Session State

```python
# Initialize ONCE (this if-check survives reruns)
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button("Click me"):
    st.session_state.count += 1

st.write(f"Clicked {st.session_state.count} times")
```

`st.session_state` is a dict that PERSISTS across reruns.
This is your survival tool. Guard it with your life.

---

## 🔐 LOGIN GOTCHAS: The Authentication Gauntlet

### Problem: "Login works but then immediately logs out"

You probably wrote:

```python
logged_in = False  # THIS RESETS EVERY RERUN

if st.button("Login"):
    logged_in = True  # Works for one millisecond

if logged_in:
    st.write("Welcome!")  # You'll never see this
```

### The Fix

```python
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.button("Login"):
    st.session_state.logged_in = True

if st.session_state.logged_in:
    st.write("Welcome!")  # NOW it persists
```

---

### Problem: "Form clears after I submit it"

This is... actually intended behavior. Streamlit reruns, form resets.

But you can work around it:

```python
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
    
    if submitted:
        # Process login here
        # Form will clear, but that's often what you want
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()  # Force rerun to show logged-in state
```

The `st.rerun()` is your friend. It forces a clean rerun after you've
updated session state.

---

### Problem: "I see both login form AND dashboard at same time"

Your logic structure is probably:

```python
# BAD: Both can render in same run
if not logged_in:
    show_login()
if logged_in:
    show_dashboard()
```

### The Fix: Proper Conditional Structure

```python
# GOOD: Only one renders
if st.session_state.get('logged_in', False):
    show_dashboard()
else:
    show_login()
```

Or use `st.rerun()` after login to force a clean slate.

---

## 📝 FORM MYSTERIES: Input Handling Secrets

### Problem: "My function runs on every keystroke"

```python
# BAD: Runs constantly as user types
name = st.text_input("Name")
if name:
    expensive_function(name)  # OH NO
```

### The Fix: Use Forms

```python
# GOOD: Only runs on submit
with st.form("my_form"):
    name = st.text_input("Name")
    if st.form_submit_button("Submit"):
        expensive_function(name)  # Only when they click
```

Forms batch inputs and only trigger on explicit submit.

---

### Problem: "Password shows as plain text"

```python
# You forgot the type parameter
password = st.text_input("Password")  # VISIBLE TO ALL

# Fixed
password = st.text_input("Password", type="password")  # Hidden
```

---

### Problem: "Checking if user exists is case-sensitive"

```python
# "Admin" and "admin" are different users
if username in st.session_state.users:
    # Might miss the user

# Better
if username.lower() in {u.lower() for u in st.session_state.users}:
    # Case-insensitive check
```

---

## 🎨 LAYOUT MYSTERIES: Making It Look Less Terrible

### Problem: "Everything is in one narrow column"

Streamlit defaults to centered, narrow content. Use columns:

```python
col1, col2 = st.columns(2)

with col1:
    st.metric("Score A", "78%")
    
with col2:
    st.metric("Score B", "92%")
```

For more columns: `st.columns([1, 2, 1])` (proportional widths)

---

### Problem: "I want tabs for Login/Register"

```python
tab1, tab2 = st.tabs(["Login", "Register"])

with tab1:
    # Login form here
    
with tab2:
    # Registration form here
```

Note: Both tabs render even if hidden. Session state works across tabs.

---

### Problem: "How do I set a page title?"

Put this at the TOP of your script (must be first Streamlit command):

```python
st.set_page_config(
    page_title="Citizen Wellness Portal™",
    page_icon="🏛️",
    layout="wide"  # or "centered"
)
```

---

## 🐛 ERROR TRANSLATION GUIDE

### "StreamlitAPIException: st.session_state can only be accessed inside a function"

You tried to access session_state at module level before any Streamlit
commands ran. Move it inside your main logic.

### "RerunException"

You called `st.rerun()` somewhere. This is intentional behavior, not an
error—it's how Streamlit forces a fresh render.

### "DuplicateWidgetID"

Two widgets have the same key. Add unique `key` parameters:

```python
st.button("Click", key="button_1")
st.button("Click", key="button_2")  # Same label, different key
```

### "Widget changed after rendering"

You tried to modify session_state for a widget that already rendered.
Structure your code so state changes happen BEFORE the widget renders.

### Form-related errors about submit buttons

- Forms need EXACTLY ONE submit button inside them
- Submit button must be `st.form_submit_button()`, not `st.button()`
- Can't nest forms

---

## 🔧 DEBUGGING STRATEGIES

### The Print Statement (Old Reliable)

```python
st.write("DEBUG: logged_in =", st.session_state.get('logged_in'))
st.write("DEBUG: users =", st.session_state.get('users', {}))
```

Ugly, but shows you what's actually in state.

### The Session State Inspector

Add this temporarily to see ALL session state:

```python
st.write("Session State:", dict(st.session_state))
```

### The Sidebar Debug Panel

Keep debug info out of main view:

```python
with st.sidebar:
    st.write("🔧 Debug Info")
    st.write(dict(st.session_state))
```

---

## 💡 PRO TIPS FROM THE RESISTANCE

### Tip 1: Initialize ALL State at the Top

```python
# Do this FIRST, before any UI
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'users' not in st.session_state:
    st.session_state.users = {}
```

### Tip 2: Use Functions for Organization

```python
def show_login():
    st.header("Login")
    # login form code

def show_dashboard():
    st.header("Dashboard")
    # dashboard code

# Main logic
if st.session_state.logged_in:
    show_dashboard()
else:
    show_login()
```

### Tip 3: The Logout Pattern

```python
def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.rerun()

if st.button("Logout"):
    logout()
```

### Tip 4: Callback Functions for Buttons

```python
def on_login_click():
    st.session_state.logged_in = True
    st.session_state.username = st.session_state.login_username

st.text_input("Username", key="login_username")
st.button("Login", on_click=on_login_click)
```

Callbacks run BEFORE the rerun, so state is updated first.

---

## 📚 RESOURCES FOR THE LOST

**Official Docs (Actually Good):**
- Session State: https://docs.streamlit.io/library/api-reference/session-state
- Forms: https://docs.streamlit.io/library/api-reference/control-flow/st.form
- Layout: https://docs.streamlit.io/library/api-reference/layout

**When Desperate:**
- Streamlit Forum: https://discuss.streamlit.io
- The Algorithm's LLM of choice (you know who)

---

## 🎭 REMEMBER

Streamlit is weird because it's optimized for a different use case than
Flask. It trades flexibility for speed.

You're not stupid if it confuses you.
Every Flask developer has the same moment of "wait, WHAT?"
The rerun model is genuinely counterintuitive at first.

But once it clicks, you can build dashboards in 20 minutes that would
take hours in Flask. That's the tradeoff.

Trust the process. Trust the session_state.
And when in doubt, `st.write()` everything.

// END TRANSMISSION //

---

```
 ____  _                _____                _         
/ ___|| |_ __ _ _   _  |  ___| __ ___  ___| |_ _   _ 
\___ \| __/ _` | | | | | |_ | '__/ _ \/ __| __| | | |
 ___) | || (_| | |_| | |  _|| | | (_) \__ \ |_| |_| |
|____/ \__\__,_|\__, | |_|  |_|  \___/|___/\__|\__, |
                |___/                          |___/ 
            Stay Coded. Stay Hidden.
```

*The resistance provides. The Algorithm approves (of your learning).*
