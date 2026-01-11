# 📋 Job Application Management System

> **Universal Prompt for AI Agents**: This workspace helps Ranvir Thind manage job applications, resumes, and application materials. Any AI agent working here should read this file first for context.

---

## 🚀 QUICK START: When User Shares a Job Link

**When Ranvir says something like:**
> "Here is the job [URL] - need info and resume"

**AI Agent must do ALL of these steps:**

### Step 1: Fetch Job Info
- Navigate to the job URL using browser tools
- Extract: Company, Position, Requirements, Keywords, Application Questions

### Step 2: Create Application Folder
```powershell
# Folder format: YYYY-MM-DD_Company_Position
mkdir "D:\Job Applications\applications\2025-12-25_CompanyName_PositionTitle"
```

### Step 3: Save Job Description
- Create `job-description.md` in the folder with full JD details
- Note key requirements and keywords to incorporate

### Step 4: Create Tailored Resume
1. Read `PROFILE.md` and `resumes/master-resume.md`
2. Create resume matching job keywords
3. Save as: `Thind, Ranvir - [Company] [Position] Resume.md`
4. **Generate PDF immediately:**
   ```powershell
   npx md-to-pdf "Thind, Ranvir - [Company] [Position] Resume.md"
   ```
5. **VERIFY ONE PAGE:**
   ```powershell
   Select-String -Path "*.pdf" -Pattern "/Count"
   # Must show: /Count 1
   # If /Count 2+, trim content and regenerate!
   ```

### Step 5: Answer Application Questions (if any)
- Save to `questions.md` in the folder
- Use STAR format for behavioral questions
- Match Ranvir's voice (see Writing Style section)

### Step 6: Update Tracker
- Add entry to `tracker.md`

### Step 7: Confirm to User
Tell user:
- ✅ Job description saved
- ✅ Resume created (MD + PDF)
- ✅ PDF verified as ONE PAGE
- ✅ Questions answered (if applicable)
- 📄 Files ready in: `applications/[folder]/`

### 📌 Reference Example
See working example at:
`applications/2025-12-25_Mitratech_ExpenseFPAAnalyst/Thind, Ranvir - Mitratech Expense FPA Analyst Resume.md`

This resume is:
- ✅ 50 lines in .md file
- ✅ Verified `/Count 1` (one page PDF)
- ✅ Bold metrics throughout
- ✅ 6 bullets per role
- ✅ Clean visual structure with `---` dividers

**Copy this format exactly for new resumes.**

---

## 🚨 CRITICAL REMINDER FOR ALL AI AGENTS

### You MUST create PDF versions of all resumes!

**Ranvir cannot upload .md files to job applications. He needs .pdf files.**

After creating any resume, ALWAYS run:
```powershell
npx md-to-pdf "Thind, Ranvir - [Company] [Position] Resume.md"
```

**If you don't create the PDF, the resume is useless.**

---

## ⚠️ CRITICAL: Writing Style Guidelines

**This system exists to save time and improve time management, NOT to replace Ranvir's voice.**

### AI Agents MUST:
1. **Write like Ranvir, not like AI** – No corporate buzzwords, no overly polished language
2. **Keep it direct and confident** – He's straightforward, not flowery
3. **Use natural language** – If it sounds like ChatGPT wrote it, rewrite it
4. **Maintain authenticity** – Real experiences, genuine tone, human imperfections are okay
5. **Reference `PROFILE.md`** for voice samples and phrasing preferences

### 🚫 NO DASHES RULE (CRITICAL):
**Never use em dashes (—) or en dashes (–) in resumes or cover letters.**

❌ BAD: "Strategy and finance professional—building with AI tools—ready to contribute"  
❌ BAD: "$1.45M–$1.75M valuation"  
❌ BAD: "June 2024 – Present"

✅ GOOD: "Strategy and finance professional with 4+ years turning complex analysis into clear recommendations"  
✅ GOOD: "$1.45M to $1.75M valuation"  
✅ GOOD: "June 2024 to Present"

**Why:** Dashes look robotic and AI generated. Use commas, "to", or restructure sentences instead.

### Red Flags to Avoid:
❌ "I am excited to leverage my synergies..."  
❌ "Spearheaded transformational initiatives..."  
❌ "Passionate about driving holistic solutions..."  
❌ Overly formal or stiff phrasing  
❌ Every sentence starting with "I"
❌ Em dashes and en dashes anywhere
❌ "Actionable insights" or "data driven decisions" without specifics
❌ Starting bullets with "Successfully" or "Effectively"

### Good Examples:
✅ "I drove 15 to 20% returns through financial modeling" – Direct, factual, no dashes  
✅ "Built dashboards that cut reporting time by 80%" – Shows action plus result  
✅ "I'm drawn to [Company] because..." – Natural, personal
✅ "June 2024 to Present" – Clean date format

---

## 📐 CRITICAL: Resume Formatting Rules

**All resumes MUST be ONE PAGE. No exceptions.**

### Formatting Requirements:

1. **ONE PAGE ONLY** – If it doesn't fit, cut content or tighten wording
2. **Bullet points = ONE LINE each** – No wrapping to second line
3. **No orphan words** – Never have 1-2 words spill to next line
4. **Concise language** – Every word must earn its place
5. **3-5 bullets per role** – Quality over quantity

### Bullet Point Rules:

**❌ BAD - Too long, wraps to second line:**
```
- Drove 15-20% client returns through comprehensive financial modeling and variance analysis, identifying performance gaps and recommending strategic improvements
```

**✅ GOOD - Fits on one line:**
```
- Drove 15-20% client returns through financial modeling and variance analysis
```

### How to Keep Bullets Short:

| Instead of... | Write... |
|---------------|----------|
| "through comprehensive financial modeling and variance analysis" | "via financial modeling and variance analysis" |
| "resulting in significant improvements to" | "improving" |
| "in order to achieve better outcomes" | "to improve" |
| "across multiple client engagements" | "for multiple clients" |
| "identifying performance gaps and recommending improvements" | (cut - implied by results) |

### One-Page Resume Structure (FULL PAGE - Not Sparse):

```
HEADER:      Name, Contact, LinkedIn                    (3 lines)
SUMMARY:     2-3 impactful sentences                    (3 lines)
EXPERIENCE:  2 roles × 6 bullets each                   (18-20 lines)
EDUCATION:   Degree, GPA, Relevant Coursework           (4 lines)
SKILLS:      4 categories, inline format                (4 lines)
─────────────────────────────────────────────────────────
TOTAL:       ~40-50 lines in .md = FULL one-page PDF
```

### 📋 RESUME TEMPLATE (Copy This Format):

```markdown
# Ranvir Singh Thind

**Seattle, WA** | rjkind01@gmail.com | (206) 771-8870 | [linkedin.com/in/ranvir-thind](https://linkedin.com/in/ranvir-thind)

---

## Professional Summary

[2-3 sentences with BOLD metrics: years experience, key skills, notable achievements. NO DASHES.]

---

## Professional Experience

**[Job Title]** | [Company] | Seattle, WA | June 2024 to Present

- [ACTION VERB] **[METRIC]** through [what you did]
- [ACTION VERB] **[METRIC]** via [method/tools used]
- [Repeat 4-6 bullets, each on ONE line, bold the numbers]

**[Previous Job Title]** | [Company] | Location | June 2020 to June 2024

- [Same format: Action + Bold Metric + Method]
- [4-6 single-line bullets]

---

## Education

**University of Washington, Michael G. Foster School of Business** | Seattle, WA  
Bachelor of Arts in Business Administration, Finance | **GPA: 3.6** | Graduated Spring 2024

*Coursework:* [4-5 relevant courses matching the job]

---

## Skills

**Category 1:** Skill, Skill, Skill, Skill, Skill  
**Category 2:** Skill, Skill, Skill, Skill, Skill  
**Category 3:** Tool, Tool, Tool, Tool, Tool  
**Category 4:** Skill, Skill, Skill, Skill
```

**Key Points:**
- Use `---` horizontal rules for visual separation
- **Bold all metrics** ($, %, numbers)
- Keep each bullet to ONE line
- 5-6 bullets per role
- 4 skill categories
- ~45-55 lines total = one page PDF
- **NO DASHES anywhere** (use "to" for ranges, commas for breaks)

### 📝 REQUIRED: Font & Styling (Add to Top of Every Resume)

```yaml
---
pdf_options:
  format: Letter
  margin: 10mm 12mm
---

<style>
body { font-size: 11pt; font-family: Calibri, 'Segoe UI', Arial, sans-serif; line-height: 1.35; color: #222; }
h1 { font-size: 22pt; margin: 0 0 2px 0; font-weight: 600; }
h2 { font-size: 11pt; font-weight: 600; margin: 12px 0 6px 0; border-bottom: 1.5px solid #222; padding-bottom: 2px; text-transform: uppercase; letter-spacing: 0.5px; }
p { font-size: 11pt; margin: 3px 0; }
li { font-size: 11pt; margin: 2px 0; }
ul { margin: 4px 0; padding-left: 16px; }
hr { margin: 6px 0; border: none; border-top: 1px solid #ccc; }
strong { font-weight: 600; }
a { color: #222; text-decoration: none; }
</style>
```

**Font Rules:**
- **Body text:** 11pt Calibri (professional, readable)
- **Name:** 22pt bold
- **Section headers:** 11pt uppercase with underline
- **Line spacing:** 1.35 (compact but readable)
- **Margins:** 10mm top/bottom, 12mm left/right

**Human Writing Rules:**
- NO dashes (em dash —, en dash –) anywhere
- Use "to" for ranges: "June 2024 to Present", "$1.45M to $1.75M"
- Use commas instead of dashes for sentence breaks
- Write like a person, not a robot

### ⚠️ Academic Projects: When to Include

**INCLUDE projects if:**
- Entry-level role requiring demonstrated skills (no work experience)
- Technical role where projects show coding/analysis skills
- Job specifically asks for project experience
- Resume looks sparse without them

**SKIP projects if:**
- Strong work experience already fills the page
- Projects would push resume to 2 pages
- Job is experienced-hire (3+ years required)
- Work experience already demonstrates the same skills

**Rule: Work experience > Academic projects. If you have real-world results, prioritize those.**

### Balance: Not Too Sparse, Not Too Cramped

**❌ Too Sparse (looks empty):**
- Only 3 bullets per job
- No summary
- No projects section
- Skills on one line

**❌ Too Dense (overwhelming):**
- 8+ bullets per job
- Long paragraphs
- Tiny fonts to fit everything

**✅ Just Right:**
- 5 bullets per job (each single-line but substantive)
- 2-3 line professional summary
- 4-line skills section with categories
- 2 detailed academic projects
- Relevant coursework included

---

## 🤖 ATS Optimization (Applicant Tracking Systems)

**Most companies use software to scan resumes before a human ever sees them. Your resume MUST pass ATS filters.**

### ATS-Friendly Formatting Rules:

**DO:**
- Use standard section headers: "Experience," "Education," "Skills" (ATS looks for these)
- Include exact keywords from the job description (ATS matches keywords)
- Use simple formatting: headers, bullets, standard fonts
- Spell out acronyms at least once: "Financial Planning & Analysis (FP&A)"
- Use standard date formats: "June 2024 – Present"
- List skills in a dedicated section (ATS scans for skill keywords)

**DON'T:**
- Use tables for main content (ATS can't parse them well)
- Use images, logos, or graphics
- Use headers/footers (often ignored by ATS)
- Use fancy fonts or icons
- Use columns for critical information
- Abbreviate everything (spell out key terms)

### Keyword Optimization:

**Step 1:** Extract keywords from the job description
**Step 2:** Include exact matches naturally in your resume
**Step 3:** Put critical keywords in Skills section AND in bullet points

**Example - Job says:** "variance analysis, forecasting, Excel"
**Resume must include:** Those EXACT words, not synonyms

### ATS Checklist:
- [ ] All keywords from JD included
- [ ] Standard section headers used
- [ ] No tables in main content
- [ ] Skills section has searchable keywords
- [ ] File saved as PDF (preserves formatting)

---

## 👁️ Human Appeal: Making the Resume Stand Out

**After passing ATS, a human reviews your resume for 6-10 seconds. Make it count.**

### Visual Hierarchy (What Eyes See First):
1. **Name** – Bold, prominent at top
2. **Current/Most Recent Role** – Most important
3. **Numbers/Metrics** – Eyes jump to quantified results
4. **Company Names** – Brand recognition

### What Makes Humans Say "YES":

| Element | Impact |
|---------|--------|
| **Quantified Results** | "Increased X by 20%" beats "Improved X" |
| **Recognizable Companies** | Name-drop clients if impressive |
| **Action Verbs** | "Drove," "Built," "Led" – not "Responsible for" |
| **Relevance** | Every bullet connects to the job |
| **Clean Design** | Easy to scan in 6 seconds |

### Power Formula for Bullets:

```
[ACTION VERB] + [WHAT YOU DID] + [RESULT WITH NUMBER]
```

**Weak:** "Responsible for financial analysis"
**Strong:** "Drove 20% client returns via financial modeling and variance analysis"

### Instant Credibility Boosters:
- Dollar amounts: "$1.45M valuation," "$500K operations"
- Percentages: "20% returns," "80% time savings"
- Scale: "2,000+ clients," "10-20 truck fleet"
- Specific tools: "Excel VBA," "Salesforce CRM"
- Client/company names: "Tabletop Village LLC"

### The 6-Second Test:

Before finalizing, ask:
1. Can I understand this person's value in 6 seconds?
2. Do numbers/metrics jump out?
3. Is it obvious they're qualified for THIS job?
4. Would I want to interview this person?

---

## 🎯 Industry-Specific Resume Guidelines

### For FP&A / Finance Roles:

**Must Include:**
- Professional summary highlighting FP&A experience
- Quantified achievements (%, $, time saved)
- Technical skills: Excel (VBA), SQL, BI tools
- Keywords: forecasting, variance analysis, budgeting, modeling
- Board/executive reporting experience if any

**Structure:**
```
Summary → Experience → Education → Skills → Projects
```

**Power Words:** Drove, Led, Built, Automated, Reduced, Grew, Managed, Delivered

### For Consulting Roles:

**Must Include:**
- Client-facing experience highlighted
- Project outcomes with measurable impact
- Communication and stakeholder skills
- Problem-solving examples

**Power Words:** Partnered, Delivered, Advised, Recommended, Collaborated

### For Tech/Analytics Roles:

**Must Include:**
- Technical skills section prominent (SQL, Python, tools)
- Data-related achievements
- Automation and efficiency improvements
- Projects section with technical details

**Power Words:** Built, Engineered, Automated, Analyzed, Developed, Optimized

---

### Space-Saving Tips (When Needed):
- Use `|` separators in skills instead of tables
- Combine related items (e.g., "Excel, VBA, SQL" not separate lines)
- Trim coursework to 4-5 most relevant courses
- Academic projects: 2 detailed > 3 sparse  

---

## 🎯 Purpose

This system is designed to:
1. **Track all job applications** with status, deadlines, and notes
2. **Manage resume versions** tailored to specific roles
3. **Store job descriptions** for reference and keyword matching
4. **Handle supplemental materials** (cover letters, essays, questions)
5. **Provide context** for AI agents to give personalized advice
6. **Save time** – Ranvir uses AI to work smarter, not to fake authenticity

---

## 📁 Folder Structure

```
D:\Job Applications\
├── README.md                    # This file - start here
├── PROFILE.md                   # Candidate profile & background
├── applications/                # Individual job applications
│   └── YYYY-MM-DD_Company_Role/ # Each application gets a folder
│       ├── job-description.md   # Full JD saved here
│       ├── resume.md            # Tailored resume for this role
│       ├── cover-letter.md      # Cover letter if needed
│       ├── questions.md         # Application questions & answers
│       └── notes.md             # Interview notes, follow-ups
├── resumes/                     # Master resume versions
│   ├── master-resume.md         # Full master resume
│   ├── finance-resume.md        # Finance-focused version
│   ├── consulting-resume.md     # Consulting-focused version
│   └── tech-resume.md           # Tech/analytics version
├── templates/                   # Reusable templates
│   ├── job-template.md          # Template for saving job postings
│   ├── cover-letter-template.md # Cover letter framework
│   └── questions-template.md    # Common application questions
└── tracker.md                   # Master application tracker
```

---

## 🤖 Instructions for AI Agents

### ⚠️ MANDATORY: Always Create PDF Resumes

**Ranvir cannot use .md files for job applications. He needs PDF files to upload.**

**Every resume MUST have both:**
1. `.md` file (source/editable version)
2. `.pdf` file (THIS IS WHAT GETS UPLOADED)

**If you create a resume without the PDF, the work is incomplete and useless.**

---

### When User Provides a Job Link/Description:
1. **Read** `PROFILE.md` for candidate background
2. **Save** the job to `applications/YYYY-MM-DD_Company_Role/job-description.md`
3. **Analyze** key requirements, skills, and keywords
4. **Compare** against the candidate's profile
5. **Add** entry to `tracker.md`
6. **Create tailored resume** (see below - ALWAYS includes PDF)

### When Creating Resumes for Applications:
1. **Read** the master resume from `resumes/master-resume.md`
2. **Read** the specific job description
3. **Identify** matching skills and experiences to highlight
4. **Incorporate** keywords from the JD naturally (don't force them)
5. **Match Ranvir's voice** – direct, confident, results-focused
6. **Create the .md file**: `Thind, Ranvir - [Company] [Position] Resume.md`
7. **⚠️ IMMEDIATELY create the PDF** (see command below)
8. **Verify both files exist** before telling user it's done

### When Answering Application Questions:
1. **Review** the job requirements and company values
2. **Pull** relevant experiences from `PROFILE.md`
3. **Use STAR format** (Situation, Task, Action, Result) when applicable
4. **Write like Ranvir talks** – not stiff, not overly casual, just real
5. **Avoid AI clichés** – no "passionate about" or "excited to leverage"
6. **Save** answers to `questions.md` in the application folder

### Writing Style Checklist (Before Finalizing):
- [ ] Would Ranvir actually say this out loud?
- [ ] Does it sound like a human wrote it?
- [ ] Are there any "AI giveaway" phrases?
- [ ] Is it direct and confident, not hedging?
- [ ] Does it use specific numbers and results?

### Naming Conventions:
- **Folders**: `YYYY-MM-DD_CompanyName_RoleTitle` (e.g., `2025-12-25_Google_FinancialAnalyst`)
- **Dates**: Use ISO format (YYYY-MM-DD)
- **Status**: Applied → Phone Screen → Interview → Offer → Accepted/Rejected

### ⚠️ IMPORTANT: Resume File Naming & Creation Rules

**ALWAYS create a NEW resume file for each application. NEVER overwrite or edit existing application resumes.**

**File Naming Format:**
```
Thind, Ranvir - [Company Name] [Position Title] Resume.md
Thind, Ranvir - [Company Name] [Position Title] Resume.pdf  ← For uploading
```

**Examples:**
- `Thind, Ranvir - Mitratech Expense FPA Analyst Resume.md`
- `Thind, Ranvir - Mitratech Expense FPA Analyst Resume.pdf`
- `Thind, Ranvir - Google Financial Analyst Resume.md`
- `Thind, Ranvir - Google Financial Analyst Resume.pdf`

**Rules:**
1. Each job application gets its OWN unique resume file
2. Name follows LinkedIn format: `Last, First - Company Position Resume.md`
3. Save in the application folder: `applications/YYYY-MM-DD_Company_Role/`
4. Never delete or overwrite previous application resumes
5. Use the master resume as the SOURCE, create tailored COPIES for each job
6. **Create PDF version for uploading to job portals**

**Why:** Ranvir needs to track which resume version was sent to which company. If he gets a callback 3 weeks later, he needs to see exactly what they received.

### 📄 PDF Creation - REQUIRED FOR EVERY RESUME

**🚨 THIS IS NOT OPTIONAL. Every resume needs a PDF.**

**The .md file is the editable source. The .pdf is what Ranvir uploads to applications.**

---

**AI Agents: Run this command IMMEDIATELY after creating the .md file:**

```powershell
cd "D:\Job Applications\applications\[FOLDER_NAME]"
npx md-to-pdf "Thind, Ranvir - [Company] [Position] Resume.md"
```

**Example:**
```powershell
cd "D:\Job Applications\applications\2025-12-25_Mitratech_ExpenseFPAAnalyst"
npx md-to-pdf "Thind, Ranvir - Mitratech Expense FPA Analyst Resume.md"
```

**This automatically creates the PDF with the same name.**

---

**✅ Correct - Application folder with BOTH files:**
```
applications/2025-12-25_Company_Role/
├── job-description.md
├── questions.md
├── Thind, Ranvir - Company Position Resume.md   ← Source (editable)
└── Thind, Ranvir - Company Position Resume.pdf  ← UPLOAD THIS
```

**❌ Wrong - Missing PDF (USELESS TO RANVIR):**
```
applications/2025-12-25_Company_Role/
├── job-description.md
├── Thind, Ranvir - Company Position Resume.md   ← Can't upload this!
```

---

### 📋 Complete Resume Creation Workflow

**AI Agents must follow ALL steps:**

1. ✍️ Create the `.md` resume file with tailored content (~30-35 lines max for one-page PDF)
2. 💾 Save it to the application folder
3. 📄 **Run `npx md-to-pdf` to generate the PDF**
4. 🔍 **VERIFY PDF IS ONE PAGE** by running:
   ```powershell
   findstr /C:"/Count" "Thind, Ranvir - [Company] [Position] Resume.pdf"
   ```
   - If output shows `/Count 1` → ✅ One page (GOOD)
   - If output shows `/Count 2` or more → ❌ TRIM CONTENT AND REGENERATE
5. 📝 Update the job-description.md checklist
6. 🎉 Tell user both files are ready

**If step 4 shows more than 1 page, you MUST trim content and regenerate. Never deliver a 2-page resume.**

---

### 🔍 MANDATORY: Resume Verification Checklist

**Before telling the user the resume is done, verify ALL of these:**

#### 🚨 PAGE COUNT VERIFICATION (REQUIRED):
```powershell
findstr /C:"/Count" "Thind, Ranvir - [Company] [Position] Resume.pdf"
```
- `/Count 1` = ✅ PASS - Resume is one page
- `/Count 2+` = ❌ FAIL - Trim content and regenerate PDF

**This is the ONLY reliable way to confirm page count. Do NOT skip this step.**

#### Content Guidelines:
- [ ] .md file is ~30-40 lines (sweet spot for one-page PDF)
- [ ] If PDF shows 2 pages, content is too long - TRIM IT
- [ ] If resume looks sparse in PDF, add more content

#### Content Density Check:
- [ ] Professional Summary: 2-3 lines ✓
- [ ] Experience: 2 roles × 5 bullets each = 10 bullets total ✓
- [ ] Education: Includes coursework ✓
- [ ] Skills: 4 categories/lines ✓
- [ ] Projects: 2-3 with descriptions ✓

#### Formatting Check:
- [ ] All bullet points fit on ONE LINE (no wrapping)
- [ ] No orphan words (1-2 words on their own line)
- [ ] Consistent formatting throughout
- [ ] No excessive white space

#### If PDF Shows 2+ Pages:
- Trim bullet points to essential info
- Remove projects section entirely
- Condense skills into fewer lines
- Shorten or remove summary
- Combine date/location with role title on same line

#### If PDF Looks Too Sparse:
- Add more bullet points (up to 5 per role)
- Add brief coursework line
- Expand skills section

**Target: ~30-40 lines in .md file = Clean one-page PDF**
**Always verify with `findstr /C:"/Count"` command after generating PDF!**

### ⚠️ CRITICAL: Fill the ENTIRE Page

**No empty space. No wasted real estate. Use every inch of the page.**

If resume has empty space at bottom:
- Add more bullets to experience (up to 6 per role)
- Expand skills section with more categories
- Add 1-2 academic projects (condensed, one line each)
- Expand coursework list
- Add certifications or additional training

**The page should look FULL but not cramped. Professional density.**

#### ATS & Human Appeal Check:
- [ ] All keywords from job description included
- [ ] Numbers/metrics in most bullet points
- [ ] Action verbs start each bullet (Drove, Built, Led, Managed)
- [ ] Standard section headers (Experience, Education, Skills)
- [ ] Company/client names included for credibility
- [ ] Clean, scannable in 6 seconds
- [ ] Would YOU interview this person based on this resume?

---

## 📊 Quick Stats

| Metric | Count |
|--------|-------|
| Active Applications | 0 |
| Interviews Scheduled | 0 |
| Offers Received | 0 |

*Last Updated: 2025-12-28*

---

## 🔗 Key Links

- **LinkedIn**: [Ranvir Thind](https://www.linkedin.com/in/ranvir-thind/)
- **Target Graduation**: 2026
- **Target Roles**: Finance, Consulting, Business Analytics

---

## 💡 Usage Tips

1. **Adding a new job**: Share the job link or paste the description
2. **Resume tailoring**: Say "tailor my resume for [job]"
3. **Cover letter**: Say "write a cover letter for [job]"
4. **Track status**: Say "update [company] to [status]"
5. **Get advice**: Ask "what should I focus on for [company]?"

---

## 🧠 Philosophy: Why This System Exists

**This is about working smarter, not faking it.**

Ranvir uses AI tools to:
- **Save time** on repetitive tasks (formatting, tailoring, tracking)
- **Improve consistency** across applications
- **Focus energy** on what matters (networking, interviews, learning)
- **Stay organized** across dozens of applications

What AI does here:
- Formats and structures content
- Identifies keywords to incorporate
- Suggests improvements based on job requirements
- Tracks applications and deadlines
- Drafts content that Ranvir reviews and edits

What Ranvir still owns:
- Every experience and achievement is real
- Final review and approval of all content
- The authentic voice and personal stories
- The actual skills and knowledge

**The goal: Spend less time on logistics, more time on what actually gets jobs.**

---

*This system is designed to be persistent across sessions. All changes are saved automatically.*

