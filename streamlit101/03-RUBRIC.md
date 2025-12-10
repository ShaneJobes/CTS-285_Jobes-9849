# Citizen Wellness Portal™ — Grading Rubric
## ORANGE Clearance Assessment Protocol

---

## Grading Philosophy (Out of Character)

This rubric prioritizes **learning velocity over perfection**. We're measuring:

- Did you engage genuinely with learning a new framework?
- Did you iterate when things didn't work?
- Can you explain what your code does?
- Did you follow professional workflows?

A student who struggles, documents their struggles, and overcomes them demonstrates more growth than one who submits perfect code without evidence of learning.

---

## Point Distribution

| Category | Points | Focus |
|----------|--------|-------|
| Functional Application | 25 | Does it work? |
| Learning Documentation | 30 | Did you engage with the learning process? |
| Code Quality | 15 | Is it readable and organized? |
| Git Workflow | 15 | Did you follow The Sacred Flow™? |
| Self-Assessment Quality | 15 | Are you accurately evaluating your own work? |
| **Total** | **100** | |

---

## Category 1: Functional Application (25 points)

### Registration System (8 points)

**8 - Fully Functional**
- New users can register successfully
- Username validation (not empty, not taken)
- Password validation (minimum length)
- Clear success/error feedback
- Form clears appropriately after success

**5 - Mostly Functional**
- Registration works for basic cases
- Some validation present but incomplete
- Feedback present but could be clearer
- Minor edge cases not handled

**2 - Partially Functional**
- Registration sometimes works
- Limited or no validation
- Poor error handling
- Confusing user experience

**0 - Non-Functional**
- Registration does not work
- Application crashes on registration attempt

### Login System (8 points)

**8 - Fully Functional**
- Registered users can log in
- Correct credentials grant access
- Wrong credentials show clear error
- Session state properly tracks login status
- Login persists across Streamlit reruns

**5 - Mostly Functional**
- Login works for basic cases
- Session state mostly working
- Some edge cases cause issues
- Error messages present but basic

**2 - Partially Functional**
- Login sometimes works
- Session state issues (resets unexpectedly)
- Poor error handling

**0 - Non-Functional**
- Login does not work

### Dashboard & Logout (9 points)

**9 - Fully Functional**
- Dashboard only visible when logged in
- Displays logged-in user's name
- Shows metrics (format and values appropriate)
- Logout button works
- Logout clears session and returns to login
- Clean, professional appearance

**6 - Mostly Functional**
- Dashboard displays after login
- Basic metrics shown
- Logout works
- Some UI polish missing

**3 - Partially Functional**
- Dashboard shows but has issues
- Metrics display problems
- Logout may not fully clear state

**0 - Non-Functional**
- No dashboard or completely broken

---

## Category 2: Learning Documentation (30 points)

This is the most important category. It demonstrates you can learn new technologies with AI assistance—a critical professional skill.

### Prompt Quality and Iteration (15 points)

**15 - Exemplary Learning Process**
- 5+ distinct prompts documented
- Clear progression from basic to advanced concepts
- Shows iteration: initial prompt → refined prompt → result
- Explains why prompts were refined
- Demonstrates genuine curiosity and exploration

**10 - Solid Learning Engagement**
- 3-4 prompts documented
- Some iteration evident
- Prompts address different aspects of the problem
- Basic explanation of what was learned

**5 - Minimal Documentation**
- 1-2 prompts documented
- Little to no iteration
- Surface-level engagement
- Missing explanations

**0 - No Documentation**
- PROCESS.md missing or empty

### Challenges and Resolutions (10 points)

**10 - Thorough Problem-Solving Documentation**
- Multiple challenges documented
- Clear description of what went wrong
- Explains the debugging/resolution process
- Shows persistence and problem-solving skills
- Includes what you tried that DIDN'T work

**7 - Adequate Problem Documentation**
- Some challenges documented
- Basic resolution explanations
- Shows some debugging effort

**3 - Minimal Problem Documentation**
- Few challenges mentioned
- Vague resolutions
- Doesn't show process

**0 - No Challenge Documentation**
- No challenges mentioned (unlikely if you did the work)

### Reflection and Insights (5 points)

**5 - Thoughtful Reflection**
- Compares Flask and Streamlit meaningfully
- Identifies what was surprising or confusing
- Discusses what you'd do differently
- Shows metacognition about your learning process

**3 - Basic Reflection**
- Some comparison between frameworks
- Surface-level observations
- Limited self-awareness

**1 - Minimal Reflection**
- Very brief or superficial
- No real insights

---

## Category 3: Code Quality (15 points)

### Organization and Readability (8 points)

**8 - Professional Quality**
- Code is well-organized (logical sections)
- Meaningful variable names
- Functions used where appropriate
- Comments explain non-obvious logic
- Consistent formatting

**5 - Adequate Quality**
- Mostly organized
- Reasonable naming
- Some comments
- Minor inconsistencies

**2 - Poor Quality**
- Disorganized code
- Unclear naming
- No comments
- Hard to follow

### Error Handling (7 points)

**7 - Robust Error Handling**
- All user inputs validated
- Clear error messages for users
- No crashes on unexpected input
- Graceful handling of edge cases

**4 - Basic Error Handling**
- Some validation present
- Basic error messages
- May crash on unusual inputs

**1 - Minimal Error Handling**
- Little to no validation
- Poor error messages
- Crashes possible

---

## Category 4: Git Workflow (15 points)

### Issue Creation (4 points)

**4 - Complete Issue**
- Created before coding started
- Clear title and description
- Deliverables listed
- Technical approach outlined

**2 - Partial Issue**
- Issue exists but incomplete
- Missing some required sections

**0 - No Issue**
- No issue created

### Commit Quality (6 points)

**6 - Excellent Commit History**
- Multiple atomic commits
- Clear, descriptive messages
- Follows commit message format
- Logical progression of work

**4 - Adequate Commits**
- Several commits present
- Messages mostly clear
- Some large commits

**2 - Poor Commits**
- Few commits or one large commit
- Unclear messages

### Pull Request (5 points)

**5 - Complete PR**
- Descriptive title
- Summary of changes
- Testing checklist completed
- Links to issue
- Learning highlights included

**3 - Adequate PR**
- Basic description
- Some required elements

**1 - Minimal PR**
- PR exists but minimal description

---

## Category 5: Self-Assessment Quality (15 points)

### Accuracy of Self-Evaluation (8 points)

**8 - Accurate and Honest**
- Self-scores closely match instructor assessment
- Honest about weaknesses
- Doesn't over- or under-estimate
- Shows good judgment

**5 - Mostly Accurate**
- Self-scores reasonable
- Some over/under estimation
- Generally honest

**2 - Inaccurate**
- Significant mismatch with actual quality
- Unable to evaluate own work objectively

### Justification Quality (7 points)

**7 - Well-Justified**
- Each score explained with evidence
- Points to specific examples in submission
- Thoughtful reasoning

**4 - Adequately Justified**
- Some explanation provided
- Basic reasoning

**1 - Poorly Justified**
- Little to no explanation
- Just numbers without reasoning

---

## Bonus Points (Up to 10 extra)

- **Helping Others (+3):** Evidence of helping classmates in discussion/Slack
- **Extension Features (+3):** Implemented optional challenges (persistent storage, hashing, etc.)
- **Exceptional Documentation (+2):** PROCESS.md could serve as a tutorial for others
- **Creative Polish (+2):** Added thoughtful UI/UX improvements beyond requirements

---

## Grade Scale

| Points | Grade | Meaning |
|--------|-------|---------|
| 90-100+ | A | Exceptional learning demonstration |
| 80-89 | B | Solid work, good learning engagement |
| 70-79 | C | Meets requirements, adequate learning shown |
| 60-69 | D | Significant gaps in functionality or documentation |
| Below 60 | F | Major requirements not met |

---

## Notes for Students

### What Earns High Marks

- Genuine engagement with learning (not just copying AI output)
- Documentation of struggles AND how you overcame them
- Evidence of iteration and refinement
- Honest self-assessment
- Clean, professional workflow

### What Loses Points

- Submitting code you can't explain
- Empty or minimal PROCESS.md
- Skipping Git workflow steps
- Over-inflated self-assessment scores
- Single commit with everything

### The Most Important Question

When grading, we ask: "Did this student learn to learn a new framework?"

A working app with no process documentation suggests copying, not learning.
A buggy app with extensive documentation of the learning journey shows genuine growth.

We value the journey as much as the destination.
