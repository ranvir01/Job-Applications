# 📐 Universal Resume Formatting Rules

## 🚨 CRITICAL: FILL EVERY LINE TO 90-100% CAPACITY

**An "orphaned word" is a single word alone on the last line of a paragraph or section.**

**THE GOLD STANDARD:** Fill each line to 90-100% capacity for maximum visual impact and information density.

### **Goal: MAXIMUM Line Fill**
- ❌ BAD: 1-3 words on last line (~20-40% full - looks incomplete)
- ⚠️ OKAY: 4-5 words on last line (~60-70% full - acceptable but not optimal)
- ✅ PERFECT: 6-10 words on last line (90-100% full - professional and complete)

### ❌ BAD - Orphaned Words:
```
Financial Analyst with 4+ years of experience in financial modeling, forecasting, and
reporting. Track record of maintaining accurate financial records, supporting month-end
close, and improving processes through automation. Strong attention to detail with
advanced Excel skills and ability to work independently with limited supervision.
Experience managing multiple projects and collaborating cross-functionally with accounting and
leadership.  ← ORPHAN!
```

### ✅ GOOD - Full Lines:
```
Financial Analyst with 4+ years of experience in financial modeling, forecasting, and
reporting. Track record of maintaining accurate financial records, supporting month-end
close, and improving processes through automation. Strong attention to detail with
advanced Excel skills and ability to work independently with limited supervision. Skilled
at managing multiple projects and collaborating cross-functionally with accounting,
operations, and leadership teams.  ← Line is 80%+ full!
```

### 🌟 BEST - Maximum Fill (90-100%):
```
Financial Analysis: Forecasting, Cash Flow Analysis, Balance Sheet Metrics, Financial
Modeling, Variance Analysis, Scenario Planning, Budgeting, P&L Analysis, EBITDA Multiples,
DCF Modeling, Sensitivity Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
← Last line is 95%+ full - PERFECT visual balance and maximum information density!
```

---

## 🔧 How to Fix Orphaned Words

### **Method 1: Add Words (Preferred - MAXIMIZE the Line!)**
Add relevant skills, details, or context to fill the line to 90-100% capacity.

**Example:**
- ❌ "...Budgeting" (1 word, ~15% of line)
- ⚠️ "...Budgeting, P&L Analysis" (2 words, ~35% of line)
- 🟡 "...Budgeting, P&L Analysis, EBITDA Multiples" (4 words, ~70% of line - good but can be better)
- ✅ "...P&L Analysis, EBITDA Multiples, DCF Modeling, Sensitivity Analysis" (6 words, ~95% of line - PERFECT!)

### **Method 2: Remove Words**
If adding isn't possible, remove less critical words to reflow text.

**Example:**
- ❌ "...through financial analysis, variance reporting, and data-driven recommendations"
- ✅ "...via financial analysis, variance reporting, and recommendations"

### **Method 3: Rephrase**
Rewrite the sentence to naturally end with multiple words.

**Example:**
- ❌ "Detail-Oriented, Multi-Project Management, Independent Execution, Cross-Functional Collaboration"
- ✅ "Detail-Oriented, Multi-Project Management, Independent Execution, Cross-Functional Collaboration, Ownership Mindset"

---

## 📏 Line Length Guidelines

### **Bullet Points:**
- **Maximum:** 95 characters (including spaces)
- **Optimal:** 85-92 characters
- **Must fit:** Single line in PDF

### **Paragraph Text:**
- **Professional Summary:** 4-5 lines total
- **Skills Lines:** Each category should end with 2+ words on last line
- **No single-word orphans:** Ever. Period.

---

## ✅ Verification Process

### **Step 1: Generate PDF**
```bash
google-chrome --headless --disable-gpu \
  --print-to-pdf="output.pdf" \
  --no-pdf-header-footer \
  "input.html"
```

### **Step 2: Extract Text with Line Numbers**
```bash
pdftotext "output.pdf" - | cat -n
```

### **Step 3: Check for Orphans**
Look at the end of each section:
- Professional Summary (lines 3-8)
- Technical Skills (last ~8 lines)
- Any multi-line content

**Red flags:**
- Single word alone on a line
- Very short last lines (< 20 characters)
- Unbalanced text distribution

### **Step 4: Verify Page Count**
```bash
pdfinfo "output.pdf" | grep Pages
```
Must show: `Pages: 1`

---

## 📋 Section-Specific Rules

### **Professional Summary**
- **Length:** 4-5 lines in PDF
- **Last line:** MUST have 3+ words
- **Fix:** Add personality traits, soft skills, or expand on collaboration
- **Examples to add:**
  - "operations, and leadership teams" (not just "leadership")
  - "Skilled at managing..." (not just "Experience managing...")
  - "with strong communication abilities" (add soft skill)

### **Technical Skills**
Each category line should end with multiple words:

**Financial Analysis:**
- ❌ Ends with: "Analysis" (1 word - orphan)
- ⚠️ Ends with: "Planning, Budgeting" (2 words - ~30% full)
- 🟡 Ends with: "Budgeting, P&L Analysis, EBITDA Multiples" (5 words - ~75% full - good)
- ✅ Ends with: "P&L Analysis, EBITDA Multiples, DCF Modeling, Sensitivity Analysis" (6 words - ~95% full - PERFECT!)

**Reporting & Compliance:**
- ❌ Ends with: "Reconciliations" (1 word - orphan)
- ⚠️ Ends with: "Dashboard Creation, KPI Tracking" (3 words - ~40% full)
- 🟡 Ends with: "KPI Tracking, Executive Reporting, Board Packages" (5 words - ~75% full - good)
- ✅ Ends with: "Board Packages, Financial Projections, OPEX Reporting" (5 words - ~90% full - PERFECT!)

**Technical Tools:**
- ❌ Ends with: "Tableau" (1 word - orphan)
- ⚠️ Ends with: "Tableau, Salesforce" (2 words - ~30% full)
- 🟡 Ends with: "PowerPoint, Tableau, Salesforce, Google Suite" (4 words - ~70% full - good)
- ✅ Ends with: "Tableau, Salesforce, Google Suite, Microsoft Office" (5 words - ~90% full - PERFECT!)

**Work Style:**
- ❌ Ends with: "Collaboration" (1 word - orphan)
- ⚠️ Ends with: "Mindset, Results-Driven" (2 words - ~35% full)
- 🟡 Ends with: "Results-Driven, Analytical Problem-Solver" (3 words - ~65% full - good)
- ✅ Ends with: "Analytical Problem-Solver, Process Improvement Focused" (4 words - ~95% full - PERFECT!)

---

## 🎯 Skills to Add (Based on Profile)

When you need to extend a line, add these relevant skills:

### **Financial Analysis:**
- Scenario Planning
- Budgeting
- EBITDA Analysis
- IRR Calculations
- Sensitivity Analysis
- P&L Analysis

### **Reporting & Compliance:**
- Dashboard Creation
- KPI Tracking
- Executive Reporting
- Board Packages
- Audit Support
- Internal Controls

### **Technical Tools:**
- Salesforce (CRM experience)
- Python (programming)
- INDEX/MATCH (Excel function)
- Google Suite
- RStudio
- Figma

### **Work Style:**
- Ownership Mindset
- Results-Driven
- Client-Focused
- Analytical Thinker
- Problem Solver
- Team Collaborator
- Entrepreneurial
- Process-Oriented

---

## 🤖 AI Agent Instructions

### **MANDATORY CHECKS BEFORE FINALIZING:**

1. **Generate PDF** from HTML
2. **Extract text** with line numbers
3. **Scan for orphans** in:
   - Professional Summary (last line)
   - Each Technical Skills category (last line)
   - Any paragraph text
4. **If orphan found:**
   - Add relevant skill/word from approved list
   - Regenerate PDF
   - Re-check
5. **Verify:**
   - No orphaned words ✓
   - One page only ✓
   - All bullets < 95 chars ✓

### **Code to Check for Orphans:**
```bash
# Extract PDF text and check last lines of each section
pdftotext "resume.pdf" - | cat -n | grep -A 1 -B 1 "SUMMARY\|SKILLS"

# Look for lines with very few words at section ends
# Manual inspection required
```

---

## 📊 Visual Balance

### **Good Visual Balance:**
```
TECHNICAL SKILLS
Financial Analysis: Forecasting, Cash Flow Analysis, Balance Sheet Metrics, Financial
Modeling, Variance Analysis, Scenario Planning, Budgeting
                                                    ^^^^^^^^^ (2+ words)

Reporting & Compliance: Monthly Close Support, Financial Reporting, Audit Documentation,
Reconciliations, Dashboard Creation, KPI Tracking
                        ^^^^^^^^^^^^^^^^^^^^^^^^^ (3 words)
```

### **Bad Visual Balance:**
```
TECHNICAL SKILLS
Financial Analysis: Forecasting, Cash Flow Analysis, Balance Sheet Metrics, Financial
Modeling, Variance Analysis, Scenario Planning
Planning
^^^^^^^^ (1 word orphan - UNACCEPTABLE)
```

---

## 🎨 Typography Rules

### **Font Sizes:**
- Name (H1): 22pt
- Section Headers (H2): 11pt (bold, uppercase, underlined)
- Body text: 11pt
- All consistent

### **Line Height:**
- 1.35 for body text
- Consistent throughout

### **Spacing:**
- Header to Summary: 12pt
- Between sections: 12pt
- Between job entries: 10pt
- Between bullets: 2pt

### **Margins:**
- Page: 10mm top/bottom, 12mm left/right
- Consistent on all sides

---

## 🔍 Quality Checklist

Before declaring a resume "done":

- [ ] **No orphaned words** (checked via `pdftotext`)
- [ ] **One page only** (checked via `pdfinfo`)
- [ ] **All bullets < 95 chars** (checked manually)
- [ ] **Proper special characters** (bullets •, em dashes –)
- [ ] **Company name correct** (MyConsulting Network Inc.)
- [ ] **All metrics bolded** (15%, $500K+, 2,000+, etc.)
- [ ] **Consistent tense** (present for current, past for previous)
- [ ] **Professional email** (no nicknames)
- [ ] **Visual balance** (no awkward line breaks)
- [ ] **ATS-friendly** (no tables, images, complex formatting)

---

## 📝 Documentation Requirements

For every resume created, document:

1. **Orphan fixes applied** (what was changed and why)
2. **Skills added** (list new skills added to eliminate orphans)
3. **Character counts** (longest bullet point)
4. **Verification results** (pdftotext and pdfinfo output)

---

## 🚀 Implementation

### **In Markdown:**
```markdown
**Work Style:** Detail-Oriented, Multi-Project Management, Independent Execution, 
Cross-Functional Collaboration, Ownership Mindset, Results-Driven
```

### **In HTML:**
```html
<p><strong>Work Style:</strong> Detail-Oriented, Multi-Project Management, 
Independent Execution, Cross-Functional Collaboration, Ownership Mindset, 
Results-Driven</p>
```

### **In PDF (verified):**
```
Work Style: Detail-Oriented, Multi-Project Management, Independent Execution,
Cross-Functional Collaboration, Ownership Mindset, Results-Driven
                                                      ^^^^^^^^^^^^^^ (2 words - GOOD!)
```

---

## 🎓 Training Examples

### **Example 1: Summary Fix**

**Before:**
```
...ability to work independently with limited supervision. Experience managing 
multiple projects and collaborating cross-functionally with accounting and
leadership.
```
**Issue:** "leadership." is orphaned

**After:**
```
...ability to work independently with limited supervision. Skilled at managing 
multiple projects and collaborating cross-functionally with accounting,
operations, and leadership teams.
```
**Fix:** Added "operations, and" + changed "leadership" to "leadership teams"

### **Example 2: Skills Fix**

**Before:**
```
Technical Tools: Excel (VBA, Pivot Tables, VLOOKUP, advanced modeling), SQL,
PowerPoint, Tableau
```
**Issue:** "Tableau" might orphan depending on line width

**After:**
```
Technical Tools: Excel (VBA, Pivot Tables, VLOOKUP, INDEX/MATCH, formulas), SQL,
Python, PowerPoint, Tableau, Salesforce
```
**Fix:** Added "Python" and "Salesforce", shortened "advanced modeling" to "formulas"

---

## 🔄 Iterative Process

1. **Write content** (focus on substance)
2. **Generate PDF** (HTML → Chrome)
3. **Check orphans** (`pdftotext` + visual inspection)
4. **Fix orphans** (add skills, rephrase, or remove words)
5. **Regenerate PDF**
6. **Verify** (repeat until no orphans)
7. **Final check** (full quality checklist)

---

## 📞 Emergency Fixes

If you're stuck with an orphan and can't add skills:

### **Option 1: Synonym Swap**
- "utilizing" → "using" (saves 4 chars)
- "through" → "via" (saves 4 chars)
- "data-driven recommendations" → "recommendations" (saves 12 chars)

### **Option 2: Remove Filler**
- "and" → "," (list format)
- "the" → remove if not critical
- "very" / "really" → remove intensifiers

### **Option 3: Restructure**
- Break into two shorter sentences
- Combine with previous line
- Move content to different section

---

**Last Updated:** January 17, 2026  
**Version:** 1.0  
**Status:** MANDATORY FOR ALL RESUMES  
**Enforcement:** AI agents MUST check for orphans before finalizing
