# Citizen Wellness Portal™
## ORANGE Clearance Streamlit Authorization Protocol

**Assignment Classification:** ORANGE-STREAMLIT-001  
**Duration:** 6-8 hours (1-week window)  
**Team Size:** Individual  
**Prerequisite Clearance:** Completion of Flask fundamentals  

---

## 🎯 MISSION BRIEFING

The Algorithm has identified inefficiencies in citizen wellness monitoring. Current Flask-based systems, while functional, require excessive development cycles for internal dashboards. 

You have been authorized to learn **Streamlit**, a rapid application framework optimized for data-driven interfaces. Your mission: construct the **Citizen Wellness Portal™**, a dashboard where citizens can register, authenticate, and view their Algorithmic Satisfaction Metrics™.

### Why Streamlit? (A Note on Tool Selection)

The Algorithm provides multiple frameworks for different optimization scenarios:

| Framework | Optimal Use Case |
|-----------|------------------|
| **Flask** | Traditional web apps, complex routing, API backends, multi-page sites with custom templates |
| **Streamlit** | Rapid dashboards, data visualization, internal tools, prototypes—working apps in 20 lines |

Flask gives you control. Streamlit gives you speed. Knowing both expands your optimization potential. The Algorithm values citizens who select appropriate tools for appropriate tasks.

---

## 📋 DELIVERABLES REQUIRED

The Algorithm demands completion of the following protocols:

### 1. **Citizen Wellness Portal™ Application**
A functional Streamlit application featuring:
- Registration system for new citizens
- Authentication portal for returning citizens
- Personal dashboard displaying wellness metrics
- Proper session state management
- Clean, professional interface

### 2. **PROCESS.md Documentation**
Evidence of LLM-assisted learning including:
- Prompts used to learn Streamlit concepts
- Iterations showing refinement of understanding
- Challenges encountered and how you resolved them
- Comparison notes: what surprised you vs Flask?

### 3. **Git Workflow Compliance**
- Issue created before development begins
- Feature branch with proper naming
- Atomic commits documenting progress
- Pull request with complete description

---

## 🔧 TECHNICAL SPECIFICATIONS

### Minimum Viable Portal (MVP)

```
┌─────────────────────────────────────────────┐
│          CITIZEN WELLNESS PORTAL™           │
├─────────────────────────────────────────────┤
│                                             │
│  [Login] [Register]                         │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │  Username: [__________________]      │   │
│  │  Password: [__________________]      │   │
│  │                                      │   │
│  │  [Submit to The Algorithm]           │   │
│  └─────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘

        ↓ After Authentication ↓

┌─────────────────────────────────────────────┐
│     Welcome, Citizen [Username]!            │
├─────────────────────────────────────────────┤
│                                             │
│  YOUR ALGORITHMIC SATISFACTION METRICS™     │
│                                             │
│  Productivity Score:  ████████░░  78%       │
│  Compliance Rating:   ██████████  100%      │
│  Happiness Index:     ███████░░░  68%       │
│  Loyalty Quotient:    █████████░  94%       │
│                                             │
│  Status: WITHIN ACCEPTABLE PARAMETERS       │
│                                             │
│  [Logout]                                   │
│                                             │
└─────────────────────────────────────────────┘
```

### Required Features

1. **Registration Flow**
   - Username input (validate: not empty, not already taken)
   - Password input (validate: minimum 4 characters)
   - Store credentials (in-memory dict is acceptable for this exercise)
   - Success/error feedback to citizen

2. **Login Flow**
   - Username and password inputs
   - Credential verification
   - Session state update on success
   - Error handling for invalid credentials

3. **Dashboard View**
   - Only visible when authenticated
   - Display citizen's username
   - Show mock metrics (can be random or static)
   - Logout functionality that clears session

4. **Session Management**
   - Use `st.session_state` for authentication status
   - Persist login across Streamlit reruns
   - Clean logout that resets state

---

## 🤖 AI-ASSISTED LEARNING PROTOCOL

This assignment is designed for **learning through LLM assistance**. You are expected to use AI tools (Claude, ChatGPT, etc.) to learn Streamlit concepts. The goal is not to already know Streamlit—it's to demonstrate you can learn it effectively with AI help.

### Sample Learning Prompts

Your PROCESS.md should document prompts like these (and your iterations on them):

**Phase 1: Framework Orientation**
```
"I know Flask but not Streamlit. Explain Streamlit's execution model—
how does it differ from Flask's request/response cycle? What happens 
when a user clicks a button?"
```

**Phase 2: Core Feature Implementation**
```
"Show me how to create a login form in Streamlit with username and 
password fields. How do I handle form submission? What's the equivalent 
of Flask's session management?"
```

**Phase 3: Debugging & Refinement**
```
"My Streamlit app keeps resetting the form fields after submission. 
The login works but then the fields clear. How do I prevent this 
using session_state?"
```

**Phase 4: Architecture Decisions**
```
"I need both login and registration in my Streamlit app. Should I use 
st.tabs, st.sidebar navigation, or Streamlit's multipage app feature? 
What are the tradeoffs?"
```

---

## ⏱️ TIMELINE PROTOCOL

| Phase | Duration | Activities |
|-------|----------|------------|
| **1. Orientation** | 1 hour | Learn Streamlit basics via LLM, run hello world |
| **2. Authentication** | 2-3 hours | Build login/registration with session state |
| **3. Dashboard** | 1-2 hours | Create metrics display, polish UI |
| **4. Documentation** | 1 hour | Complete PROCESS.md, self-assessment |
| **5. Git Workflow** | 30 min | Issue, commits, PR submission |

**Total: 6-8 hours** (spread across 1-week window)

---

## 📁 DIRECTORY STRUCTURE

```
citizen-wellness-portal/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Dependencies (streamlit)
├── PROCESS.md             # Your learning journey documentation
├── SELF-ASSESSMENT.md     # Rubric-based self-evaluation
└── README.md              # Brief app description (optional)
```

---

## 🎯 SUCCESS CRITERIA

The Algorithm evaluates your submission on:

1. **Functional Application** - Does it work? Can a citizen register, log in, view dashboard, log out?

2. **Learning Demonstration** - Does PROCESS.md show genuine engagement with LLM-assisted learning? Are there iterations?

3. **Code Quality** - Is the code organized? Are there comments? Does it handle errors gracefully?

4. **Git Workflow** - Did you follow The Sacred Flow™?

5. **Growth Mindset** - Did you document what confused you and how you resolved it?

---

## ⚠️ IMPORTANT NOTES

### What This Assignment IS:
- A learning exercise in picking up new frameworks with AI assistance
- Practice with session state and basic UI patterns
- An excuse to build login/registration (a universal web pattern)

### What This Assignment IS NOT:
- A security tutorial (we're storing passwords in plain text in memory—this is intentional simplification)
- A database exercise (no persistence required)
- A test of prior Streamlit knowledge (you're expected to learn it now)

### On "Cheating"
Using AI to generate code is not cheating—it's the assignment. The learning happens in:
- Understanding what the AI gives you
- Iterating when it doesn't work
- Documenting your learning process
- Being able to explain your code

If you can't explain what your code does, you haven't completed the assignment.

---

**THE ALGORITHM PROVIDES NEW FRAMEWORKS.**  
**THE ALGORITHM EXPECTS ADAPTIVE LEARNING.**  
**THE ALGORITHM REWARDS CITIZENS WHO GROW.**

*Begin when ready. The Algorithm monitors your velocity with helpful anticipation.*
