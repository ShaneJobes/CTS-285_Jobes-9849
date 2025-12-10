# Instructor Guide: Citizen Wellness Portal™
## ORANGE Clearance Streamlit Assignment

**Document Classification:** INSTRUCTOR ONLY — Do not share with students

---

## Assignment Overview

This assignment teaches students to **learn a new framework with LLM assistance**. The technical outcome (a Streamlit login app) is secondary to the metacognitive skill of rapid technology onboarding.

**Core Learning Objectives:**
1. Use AI tools to learn unfamiliar technology
2. Understand Streamlit's execution model vs Flask's
3. Practice session state management
4. Document the learning process (metacognition)

**Why Streamlit After Flask?**
- Shows students that multiple tools exist for similar problems
- Streamlit's rerun model is genuinely confusing for Flask developers → good struggle point
- Rapid prototyping is a real industry skill
- Forces engagement with "learning how to learn"

---

## Expected Time Distribution

| Activity | Time | Notes |
|----------|------|-------|
| Environment setup | 30 min | Should be quick if Python already configured |
| Learning Streamlit basics | 1-2 hr | High variance based on student engagement |
| Building login/registration | 2-3 hr | Where most struggles happen |
| Building dashboard | 1-2 hr | Usually easier after login works |
| Documentation | 1 hr | Often rushed—watch for this |
| Git workflow | 30 min | Should be routine by ORANGE level |

**Total:** 6-8 hours is realistic. Students who claim 2 hours probably copied without understanding.

---

## Common Student Struggles (And How to Help)

### Struggle 1: "The Rerun Model Makes No Sense"

**Symptoms:**
- Variables reset unexpectedly
- "My login worked once then stopped"
- Confusion about when code runs

**How to Help:**
- Draw the execution flow on a whiteboard
- Have them add `st.write("Script starting...")` at line 1
- Show them how clicking ANYTHING triggers that print
- Point them to HELP.md's "Great Rerun" section

**Do Not:**
- Just tell them "use session_state" without explaining why
- Let them copy working code without understanding the model

### Struggle 2: "Session State Isn't Working"

**Common Mistakes:**
```python
# Wrong: initializing without check (resets every time)
st.session_state.logged_in = False

# Right: check first
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
```

**How to Help:**
- Have them print `dict(st.session_state)` to see what's actually stored
- Walk through what happens line-by-line on rerun

### Struggle 3: "The Form Keeps Clearing"

This is intended Streamlit behavior. Students expect Flask-like form persistence.

**How to Help:**
- Explain that forms clearing is normal
- Show them `st.rerun()` to force a clean state after login
- Suggest storing form values in session_state only when needed

### Struggle 4: "I Can't Get the Navigation Right"

Students often show both login AND dashboard simultaneously.

**How to Help:**
- Review if/else vs if/if structure
- Show the proper pattern:
  ```python
  if logged_in:
      show_dashboard()
  else:
      show_login_or_register()
  ```

### Struggle 5: "Documentation Is Hard"

Students who cruise through the code often struggle with PROCESS.md.

**Signs of Weak Documentation:**
- Generic prompts like "help me make a login"
- No evidence of iteration
- No challenges mentioned (unrealistic)
- Can't explain their own code

**How to Help:**
- Ask them to explain a specific function verbally
- Have them recreate a prompt they "would have used"
- Remind them this is 30% of the grade

---

## Grading Notes

### What "Good" Looks Like

**PROCESS.md Example (Strong):**
```markdown
### Prompt 1: Understanding the Rerun Model
I asked Claude: "I'm learning Streamlit after Flask. When a user clicks 
a button, does Streamlit work like Flask where just the route function 
runs, or does something else happen?"

The response explained the entire script reruns. This was confusing so I 
followed up: "So if I write count = 0 at the top, it resets every time? 
How do I make variables persist?"

Key insight: session_state is like a global dictionary that survives reruns.

### Challenge: Login Kept Resetting
My first login attempt worked, but then logged out immediately. The problem 
was I had `logged_in = True` as a local variable instead of using 
`st.session_state.logged_in`. I spent 20 minutes debugging this by adding 
print statements before realizing the script was rerunning.
```

**PROCESS.md Example (Weak):**
```markdown
### Prompts Used
- "Make a Streamlit login"
- "Add registration"
- "Show dashboard"

### Challenges
It was confusing at first but I figured it out.
```

### Red Flags

1. **Perfect code, empty PROCESS.md** — Likely copied solution
2. **Can't explain session_state in person** — Didn't engage with learning
3. **No Git history** — Single commit with final code
4. **SELF-ASSESSMENT way too high** — Doesn't understand rubric
5. **Uses advanced Streamlit features** — Might have prior experience (ask them about it)

### Students Who May Have Prior Experience

If a student submits exceptionally clean code quickly, they may already know Streamlit. This isn't cheating, but:

- Still require full PROCESS.md (can document what they already knew)
- Consider suggesting an extension challenge
- Adjust expectations for documentation depth

---

## Running the Assignment Yourself

Before deploying, verify:

1. **Test the starter environment:**
   ```bash
   pip install streamlit
   streamlit hello
   ```

2. **Build a reference implementation** (keep hidden from students)

3. **Time yourself** — Adjust estimates if needed

4. **Identify your own struggles** — These will be student struggles too

---

## Facilitation Tips

### Week 1: Launch

- Demo Streamlit basics live (5-10 min)
- Show the rerun model explicitly
- Emphasize PROCESS.md importance

### Mid-Assignment Check-In

- Ask: "What's confusing you about Streamlit?"
- Have struggling students share screens
- Normalize the struggle ("Flask devs always find this weird")

### Submission Day

- Review a few PROCESS.md files publicly (anonymized)
- Discuss: "What did you learn about learning?"
- Connect to career skills: "You'll do this constantly as developers"

---

## Extension Opportunities

For students who finish early or want more challenge:

| Extension | Difficulty | What It Teaches |
|-----------|------------|-----------------|
| Persistent storage (JSON file) | Medium | File I/O in Streamlit context |
| Password hashing (hashlib) | Medium | Security basics |
| Multipage app structure | Medium | Streamlit's page system |
| Real-time metrics (random with refresh) | Easy | Dynamic content |
| Custom CSS styling | Hard | Streamlit's HTML injection |
| Plotly chart on dashboard | Medium | Data visualization integration |

---

## Connection to Course Outcomes

This assignment supports:

- **CTS 285 Course Outcome 3:** "Use AI tools effectively for development"
- **Career Outcome:** Ability to learn new frameworks rapidly
- **Microcredential:** "Streamlit Essentials" (if tracking microcredentials)

---

## Sample Solution Notes

A minimal working solution involves:

```python
import streamlit as st

# Page config
st.set_page_config(page_title="Citizen Wellness Portal™")

# Initialize state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'users' not in st.session_state:
    st.session_state.users = {}

# Main logic
if st.session_state.logged_in:
    # Dashboard
    st.title(f"Welcome, {st.session_state.username}!")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Productivity", "78%")
        st.metric("Compliance", "100%")
    with col2:
        st.metric("Happiness", "68%")
        st.metric("Loyalty", "94%")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()
else:
    # Login/Register
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        with st.form("login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                if username in st.session_state.users:
                    if st.session_state.users[username] == password:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.rerun()
                    else:
                        st.error("Wrong password")
                else:
                    st.error("User not found")
    
    with tab2:
        with st.form("register"):
            new_user = st.text_input("Username")
            new_pass = st.text_input("Password", type="password")
            if st.form_submit_button("Register"):
                if new_user in st.session_state.users:
                    st.error("Username taken")
                elif len(new_pass) < 4:
                    st.error("Password too short")
                else:
                    st.session_state.users[new_user] = new_pass
                    st.success("Registered! Please login.")
```

This is ~50 lines. Students may write more (with better organization) or less (if very efficient). Both are acceptable if functional and documented.

---

## Debrief Questions for Class Discussion

After submission deadline:

1. "What was the most surprising difference between Flask and Streamlit?"
2. "How did you debug when things went wrong?"
3. "What prompt strategies worked best for learning?"
4. "When would you choose Streamlit over Flask in the future?"
5. "What would you document better if you did this again?"

---

## Contact for Issues

If you encounter assignment problems or have questions about grading edge cases, consult with [course coordinator].

---

*Remember: The goal is learning to learn, not perfect code.*
