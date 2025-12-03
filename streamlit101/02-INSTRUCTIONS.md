# Citizen Wellness Portal™ — Technical Instructions
## ORANGE Clearance Development Protocol

---

## Learning Objectives (Out of Character)

By completing this assignment, you will:

- **Learn a new framework with AI assistance** — Practice the skill of rapidly onboarding to unfamiliar technology using LLM tools
- **Understand Streamlit's execution model** — Grasp how Streamlit differs from traditional request/response frameworks like Flask
- **Implement session state management** — Use `st.session_state` to persist data across reruns
- **Build authentication UI patterns** — Create login/registration flows (a universal web development skill)
- **Document your learning process** — Practice metacognition about how you learn technical concepts

**Time estimate:** 6-8 hours over 1 week

---

## Prerequisites

Before starting, ensure you have:

- [ ] Python 3.8+ installed
- [ ] Completed Flask fundamentals (you understand routes, templates, sessions)
- [ ] Access to an LLM tool (Claude, ChatGPT, etc.)
- [ ] Git configured and working

---

## Phase 1: Environment Setup (30 minutes)

### 1.1 Create Your Project Directory

```bash
mkdir citizen-wellness-portal
cd citizen-wellness-portal
```

### 1.2 Set Up Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 1.3 Install Streamlit

```bash
pip install streamlit
```

### 1.4 Verify Installation

```bash
streamlit hello
```

This should open a demo app in your browser. If it works, you're ready.

### 1.5 Create requirements.txt

```
streamlit>=1.28.0
```

---

## Phase 2: Streamlit Orientation (1 hour)

Before writing your app, spend time understanding how Streamlit works. This is fundamentally different from Flask.

### Key Concept: The Rerun Model

**Flask model:**
```
User clicks button → Browser sends request → Server runs route function → Server sends response → Page updates
```

**Streamlit model:**
```
User clicks button → ENTIRE SCRIPT RERUNS from top to bottom → Page updates
```

This means:
- Variables reset on every interaction unless stored in `st.session_state`
- There are no "routes" — your script IS the app
- UI elements are declared, not imperatively created

### Suggested Learning Prompts

Use these prompts (or variations) with your LLM. Document what you learn in PROCESS.md.

**Prompt 1: Conceptual Foundation**
```
I'm a Flask developer learning Streamlit. Explain the key differences 
in how these frameworks work. Specifically:
1. How does Streamlit handle user interactions vs Flask's routes?
2. What happens when a user clicks a button in Streamlit?
3. Why do I need st.session_state when I didn't need anything 
   special for variables in Flask?
```

**Prompt 2: Hello World Comparison**
```
Show me a simple "Hello, [name]" app in both Flask and Streamlit 
side by side. The app should:
- Have a text input for the user's name
- Display "Hello, [name]!" after they enter it
- Explain the key differences in how each version works
```

### Your Task

Create a file called `hello.py` with a simple Streamlit app:
- Text input for a name
- Button that displays a greeting
- Experiment with what happens when you interact with it

Run it with:
```bash
streamlit run hello.py
```

---

## Phase 3: Building the Login System (2-3 hours)

### 3.1 Understanding Session State

Session state is crucial. Without it, your login status resets every time the user does anything.

**Suggested Prompt:**
```
Show me how st.session_state works in Streamlit. I need to:
1. Store whether a user is logged in (boolean)
2. Store the logged-in username (string)
3. Make these persist when the user clicks buttons or interacts with the app
Include a minimal example.
```

### 3.2 Creating the Login Form

Streamlit provides `st.form()` for grouping inputs that submit together. This prevents reruns on every keystroke.

**Suggested Prompt:**
```
Create a Streamlit login form with:
- Username text input
- Password input (hidden characters)
- Submit button
- The form should not trigger reruns until the button is clicked
Show me how to access the submitted values.
```

### 3.3 Implementing Credential Storage

For this exercise, store users in a simple dictionary. This is NOT secure for production but teaches the pattern.

```python
# Example structure (you'll implement this)
if 'users' not in st.session_state:
    st.session_state.users = {}  # {'username': 'password'}
```

**Suggested Prompt:**
```
I'm building a Streamlit app with login/registration. I want to store 
users in st.session_state as a dictionary. Show me how to:
1. Initialize the users dict if it doesn't exist
2. Add a new user during registration
3. Check credentials during login
4. Handle errors (user already exists, wrong password, etc.)
```

### 3.4 Implementing Registration

Registration needs:
- Username input (check if already taken)
- Password input (minimum length validation)
- Confirm password (optional but good practice)
- Success/error messages

**Suggested Prompt:**
```
Add registration to my Streamlit login app. I need:
- Form with username, password, confirm password
- Validation: username not empty, not already taken
- Validation: password minimum 4 characters, matches confirmation
- Show success message and clear form on success
- Show error message on validation failure
Use st.success() and st.error() for feedback.
```

### 3.5 Navigation Between Login and Register

You have options for handling multiple "views":

| Approach | Pros | Cons |
|----------|------|------|
| `st.tabs()` | Simple, all on one page | Both forms always visible |
| `st.sidebar` + buttons | Clean separation | Sidebar might feel awkward |
| Session state "page" variable | Full control | More code to manage |
| Streamlit multipage | Official solution | Might be overkill for this |

**Suggested Prompt:**
```
I have login and registration forms in my Streamlit app. What's the 
best way to let users switch between them? Compare using st.tabs() 
vs using a session_state variable to track which "page" to show. 
Which is simpler for a small app like this?
```

---

## Phase 4: Building the Dashboard (1-2 hours)

### 4.1 Conditional Rendering

The dashboard should only appear when the user is logged in.

```python
# Pseudocode pattern
if st.session_state.get('logged_in', False):
    show_dashboard()
else:
    show_login_or_register()
```

### 4.2 Displaying Metrics

Streamlit has built-in components for metrics display:

```python
st.metric(label="Productivity Score", value="78%", delta="+3%")
```

**Suggested Prompt:**
```
Show me how to create a dashboard in Streamlit with:
- A welcome message showing the logged-in user's name
- 4 metric displays using st.metric() with labels and values
- A logout button that clears the session
- Use st.columns() to arrange the metrics in a grid
```

### 4.3 Mock Data

Your metrics can be:
- Static values (simplest)
- Random values generated on login (more interesting)
- Stored per-user in session state (most complete)

Pick whichever teaches you the most.

---

## Phase 5: Polish and Error Handling (1 hour)

### 5.1 User Experience Improvements

Consider adding:
- Clear feedback messages (success/error)
- Input validation with helpful messages
- A clean layout using `st.container()` or columns
- App title and basic styling via `st.set_page_config()`

**Suggested Prompt:**
```
How do I improve the appearance of my Streamlit app? Show me:
1. How to set the page title and icon with st.set_page_config()
2. How to use st.container() for layout organization
3. How to add some visual separation between sections
Keep it simple - I just want it to look professional, not fancy.
```

### 5.2 Error Handling

Make sure your app handles:
- Empty username/password submission
- Login with wrong credentials
- Registration with taken username
- Password mismatch on registration

---

## Phase 6: Documentation (1 hour)

### 6.1 Create PROCESS.md

This is the most important part of your submission. Document:

```markdown
# Learning Process Documentation

## Prompts Used and What I Learned

### Understanding Streamlit's Model
**Prompt:** [Your actual prompt]
**Key Insight:** [What clicked for you]
**Iteration:** [If you had to refine the prompt, what did you change?]

### Building the Login Form
**Prompt:** [Your actual prompt]
**Challenge:** [What didn't work at first]
**Solution:** [How you fixed it]

## Flask vs Streamlit: My Observations

[What surprised you? What's easier? What's harder?]

## Challenges and Resolutions

1. **Challenge:** [Description]
   **How I solved it:** [Description]

2. [etc.]

## What I'd Do Differently

[Reflection on your process]
```

### 6.2 Create SELF-ASSESSMENT.md

See RUBRIC.md for the criteria. Score yourself honestly and explain your reasoning.

---

## Phase 7: Git Workflow (30 minutes)

### 7.1 Create Issue

Before you start coding (ideally do this first), create an issue:

**Title:** `Citizen Wellness Portal - Streamlit Authentication System`

**Body:**
```markdown
## Overview
Building the Citizen Wellness Portal using Streamlit with login/registration.

## Deliverables
- [ ] Working Streamlit app with login/registration
- [ ] Dashboard with mock metrics
- [ ] Session state management
- [ ] PROCESS.md documenting learning journey
- [ ] SELF-ASSESSMENT.md with rubric evaluation

## Technical Approach
[Brief description of your planned approach]

## Time Estimate
6-8 hours over 1 week
```

### 7.2 Create Feature Branch

```bash
git checkout -b feature/citizen-wellness-portal
```

### 7.3 Commit Regularly

Make atomic commits as you progress:

```bash
git add app.py
git commit -m "feat(streamlit): add login form with session state"

git add app.py
git commit -m "feat(streamlit): add registration with validation"

git add app.py
git commit -m "feat(streamlit): add dashboard with metrics display"

git add PROCESS.md SELF-ASSESSMENT.md
git commit -m "docs: add learning process and self-assessment"
```

### 7.4 Create Pull Request

**Title:** `feat: Citizen Wellness Portal - Streamlit Authentication`

**Body:**
```markdown
## Summary
Implemented Citizen Wellness Portal using Streamlit framework.

## Changes
- Login/registration system with session state
- Dashboard with Algorithmic Satisfaction Metrics
- Full documentation of learning process

## Testing
- [x] Registration creates new user
- [x] Login validates credentials
- [x] Dashboard displays after login
- [x] Logout clears session
- [x] Error handling for invalid inputs

## Learning Highlights
[1-2 sentences about what you learned]

Closes #[issue-number]
```

---

## Submission Checklist

Before submitting, verify:

- [ ] `app.py` runs without errors (`streamlit run app.py`)
- [ ] Can register a new user
- [ ] Can log in with registered credentials
- [ ] Cannot log in with wrong credentials
- [ ] Dashboard shows after login with metrics
- [ ] Logout works and returns to login screen
- [ ] `requirements.txt` includes streamlit
- [ ] `PROCESS.md` documents your learning journey with actual prompts
- [ ] `SELF-ASSESSMENT.md` scores yourself against the rubric
- [ ] Git issue created and linked
- [ ] Pull request submitted with complete description
- [ ] All files in correct directory structure

---

## Getting Help

If you're stuck:

1. **Check HELP.md** for common Streamlit issues
2. **Ask your LLM** "Why isn't this working?" with the code and error
3. **Streamlit docs:** https://docs.streamlit.io
4. **Post in class discussion** (helping others also earns credit)
5. **Office hours** (no penalties for asking questions)

---

## Extension Opportunities (Optional)

If you finish early and want more challenge:

- **Persistent storage:** Save users to a JSON file
- **Password hashing:** Use `hashlib` to not store plaintext
- **Multipage app:** Use Streamlit's official multipage feature
- **Real metrics:** Track login count, last login time
- **Styling:** Custom CSS via `st.markdown()` with `unsafe_allow_html`
- **Charts:** Add a chart to the dashboard using `st.line_chart()` or Plotly
