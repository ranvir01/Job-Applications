# Resume Creation Instructions

> **FOR AI AGENTS**: Follow these instructions EXACTLY when user requests resume creation for a job.

## Trigger Phrases

When user says any of the following (with a job description), execute the full process below:
- "Create resume for this job"
- "Make a resume for this"
- "Tailor resume for this role"
- "Apply for this job"
- Or any similar request with a job description attached

---

## Automatic Process (Execute All Steps)

### Step 1: Read Required Files
```
READ: /workspace/resumes/master-resume.md (source content)
READ: /workspace/resumes/README.md (framing guidelines - CRITICAL)
```

### Step 2: Analyze Job Description
Extract and identify:
- **Company name** and **role title**
- **Required skills** (must-haves)
- **Preferred skills** (nice-to-haves)
- **Keywords** to incorporate naturally
- **Experience level** expected

### Step 3: Create Application Folder
```
CREATE FOLDER: /workspace/applications/[company-name]/
```
Use lowercase, hyphenated company name (e.g., `floqast`, `amazon`, `deloitte`)

### Step 4: Save Job Description
Save the full job description to:
```
/workspace/applications/[company-name]/job-description.md
```

### Step 5: Create Tailored Resume

**Source**: Use `master-resume.md` as the base

**Apply Universal Framing Principles** (from README.md):

| Principle | Action |
|-----------|--------|
| AI/Tool Ownership | Frame AI usage as "augmentation with human review and ownership" |
| Business-First | Lead bullets with outcomes, not tool names |
| Meaningful Scale | Describe complexity/techniques, not just row counts |
| Adaptability | Include stakeholder collaboration language |
| Ramp-Up Evidence | Show specific examples of learning quickly |
| Decision Walkthroughs | Describe questions addressed and outcomes achieved |

**Avoid Red Flag Phrases**:
- ❌ "I use AI for everything" → ✅ "Use AI to accelerate work, reviewing and owning outputs"
- ❌ "Worked with 10,000+ rows" → ✅ "Processed datasets requiring aggregation and validation"
- ❌ "Advanced Excel: VLOOKUP" → ✅ "Excel for exploratory analysis and validation"
- ❌ "I can learn any tool" → ✅ "Focus on business questions first, select appropriate tools"

**Tailoring Actions**:
1. Reorder bullets to match job priorities
2. Swap in relevant alternate bullets from master resume
3. Incorporate job keywords naturally (don't force them)
4. Adjust summary to align with role focus
5. Highlight matching skills, de-emphasize irrelevant ones

**Save as**:
```
/workspace/applications/[company-name]/resume.md
```

### Step 6: Generate PDF
```bash
npx md-to-pdf /workspace/applications/[company-name]/resume.md
```

### Step 7: Update Tracker
Add entry to `/workspace/tracker.md`:
```markdown
| [Company] | [Role] | [Date] | Applied | [Link] |
```

### Step 8: Confirm Completion
Report to user:
- ✅ Resume created: `applications/[company]/resume.md`
- ✅ PDF generated: `applications/[company]/resume.pdf`
- ✅ Job description saved
- ✅ Tracker updated
- Key tailoring decisions made

---

## Resume Format Requirements

- **Length**: 1 page maximum
- **Bullets**: Bold the lead metric/achievement
- **No dashes**: Use bullet points (-)
- **ATS-friendly**: Simple formatting, no tables in resume itself
- **Keywords**: Incorporate naturally from job description

---

## Quality Checklist (Verify Before Completing)

- [ ] All bullets lead with impact/outcome, not tool names
- [ ] AI usage framed with ownership language
- [ ] Scale described by complexity, not raw numbers
- [ ] Keywords from JD incorporated naturally
- [ ] Summary aligned with role focus
- [ ] No red flag phrases present
- [ ] PDF generated successfully
- [ ] Tracker updated

---

## Example User Prompt

User only needs to say:

```
Create resume for this job:

[Paste job description here]
```

AI Agent handles everything else automatically.

---

*Last Updated: 2025-01-20*
