# Resume Creation Guide for AI Agents

## 📌 QUICK START

**For creating new resumes, copy the template from `MASTER_RESUME_TEMPLATE.md`**

This is the perfected HTML template that produces clean, professional PDFs every time.

---

## 🎯 CRITICAL: Resume Format Standards

### **MANDATORY REQUIREMENTS**
1. ✅ **One page only** - Never exceed one page
2. ✅ **ATS-friendly** - Clean formatting, no tables, no graphics
3. ✅ **Proper encoding** - UTF-8 for special characters (bullets, em dashes)
4. ✅ **Professional fonts** - Calibri, Arial, or similar sans-serif
5. ✅ **Consistent spacing** - 11pt font, 1.35 line height
6. ✅ **Bullet points fit on ONE line** - Max ~95 characters per bullet

---

## 📋 Resume Structure (STRICT ORDER)

### 1. **Header** (3 lines max)
```
# Full Name
**City, State** | email@example.com | (XXX) XXX-XXXX | linkedin.com/in/profile
```

### 2. **Professional Summary** (3-4 lines)
- Start with job title + years of experience
- Include 3-4 key skills/achievements
- Use **bold** for numbers and key metrics
- Keep under 85 words

### 3. **Professional Experience** (2 positions max)
**Format:**
```
**Job Title** | Company Name | City, State | Month Year – Present/Month Year
```

**Bullets (5-6 per job):**
- Start with strong action verbs (Built, Drove, Delivered, Managed, Automated, Reduced)
- Include **quantifiable metrics** in bold
- Keep each bullet under 95 characters
- Focus on RESULTS, not responsibilities

### 4. **Education** (2-3 lines)
```
**University Name – School Name** | City, State
Degree Name | **GPA: X.X** | Graduated Season Year
*Relevant Coursework:* Course 1, Course 2, Course 3, Course 4
```

### 5. **Technical Skills** (4 lines)
```
**Category 1:** Skill, Skill, Skill, Skill, Skill
**Category 2:** Skill, Skill, Skill, Skill
**Category 3:** Tool (details), Tool, Tool, Tool
**Category 4:** Skill, Skill, Skill, Skill
```

---

## 🔧 Technical Implementation

### **Method 1: HTML → PDF (RECOMMENDED)**

**Step 1:** Create HTML file with this structure:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Name - Resume</title>
    <style>
        @page { size: Letter; margin: 10mm 12mm; }
        body { font-size: 11pt; font-family: Calibri, 'Segoe UI', Arial, sans-serif; 
               line-height: 1.35; color: #222; margin: 0; padding: 0; }
        h1 { font-size: 22pt; margin: 0 0 2px 0; font-weight: 600; }
        h2 { font-size: 11pt; font-weight: 600; margin: 12px 0 6px 0; 
             border-bottom: 1.5px solid #222; padding-bottom: 2px; 
             text-transform: uppercase; letter-spacing: 0.5px; }
        p { font-size: 11pt; margin: 3px 0; }
        li { font-size: 11pt; margin: 2px 0; }
        ul { margin: 4px 0; padding-left: 16px; }
        strong { font-weight: 600; }
        em { font-style: italic; }
        a { color: #222; text-decoration: none; }
    </style>
</head>
<body>
    <!-- Resume content here -->
</body>
</html>
```

**Step 2:** Convert to PDF using Chrome:
```bash
google-chrome --headless --disable-gpu \
  --print-to-pdf="output.pdf" \
  --no-pdf-header-footer \
  "input.html"
```

### **Method 2: Markdown → HTML → PDF**

**Markdown Template:**
```markdown
---
pdf_options:
  format: Letter
  margin: 10mm 12mm
---

<style>
/* Same CSS as above */
</style>

# Full Name

**City, State** | email | phone | [linkedin](url)

## Professional Summary

Content here with **bold metrics**...

## Professional Experience

**Job Title** | Company | Location | Dates

- Bullet point with **metrics**
- Another bullet with **results**

## Education

**University** | Location
Degree | **GPA** | Graduated Date

*Relevant Coursework:* List courses

## Technical Skills

**Category:** Skills list
```

---

## ✍️ Writing Guidelines

### **Bullet Point Rules**
1. **Length:** Max 95 characters (including spaces)
2. **Structure:** Action Verb + What + Result/Metric
3. **Metrics:** Always bold numbers and percentages
4. **Specificity:** Use exact numbers, not ranges when possible

### **Good Examples:**
```
✅ Drove **15-20% client returns** via financial analysis and variance reporting
✅ Automated CRM reporting for **2,000+ accounts**, improving efficiency by **30%**
✅ Reduced operational costs by **10%** through process improvement analysis
```

### **Bad Examples:**
```
❌ Drove 15-20% client returns through financial analysis, variance reporting, and data-driven recommendations (TOO LONG)
❌ Responsible for managing multiple projects (NO METRICS)
❌ Helped with month-end close processes (WEAK VERB)
```

### **Action Verbs by Category:**

**Leadership:** Led, Directed, Managed, Coordinated, Supervised
**Achievement:** Drove, Delivered, Achieved, Exceeded, Increased
**Creation:** Built, Developed, Created, Designed, Established
**Improvement:** Automated, Streamlined, Optimized, Enhanced, Reduced
**Analysis:** Analyzed, Evaluated, Assessed, Identified, Forecasted
**Communication:** Presented, Collaborated, Partnered, Communicated

---

## 🎨 Visual Formatting Best Practices

### **Spacing:**
- Header to Summary: 12pt
- Between sections: 12pt
- Between job titles: 10pt
- Between bullets: 2pt
- Line height: 1.35

### **Font Sizes:**
- Name (H1): 22pt
- Section Headers (H2): 11pt (uppercase, underlined)
- Body text: 11pt
- All consistent, no variation

### **Emphasis:**
- **Bold:** Metrics, job titles, company names, key achievements
- *Italic:* Only for "Relevant Coursework" label
- Regular: Everything else

### **Alignment:**
- Everything left-aligned
- No centering except optionally the name
- Consistent left margin (10-12mm)

---

## 🔍 Quality Checklist

Before finalizing ANY resume, verify:

- [ ] **🚨 LINES FILLED TO 90-100% CAPACITY** (maximize every line - see FORMATTING_RULES.md)
- [ ] **One page only** (check with `pdfinfo file.pdf | grep Pages`)
- [ ] **No line wrapping** in bullets (check with `pdftotext`)
- [ ] **All metrics bolded** (15%, $500K+, 2,000+, etc.)
- [ ] **Proper special characters** (bullets •, em dashes –, not ?)
- [ ] **Company name correct** (MyConsulting Network Inc., not Independent Contractor)
- [ ] **Visual balance** (each section ends with 2+ words on last line)
- [ ] **Consistent tense** (past for old jobs, present for current)
- [ ] **No typos** (spell check everything)
- [ ] **ATS-friendly** (no tables, images, or complex formatting)
- [ ] **Professional email** (no nicknames or unprofessional addresses)

**CRITICAL:** Check that lines are filled to 90-100% capacity using:
```bash
pdftotext "resume.pdf" - | cat -n | tail -15
```
Look at lines ending sections - should have 6-10 words on final line (90-100% full), not just 1-3 words.

---

## 🚨 Common Mistakes to Avoid

### **Content Mistakes:**
1. ❌ Using "Responsible for" instead of action verbs
2. ❌ Listing duties instead of achievements
3. ❌ Missing metrics and quantification
4. ❌ Inconsistent tense (mixing past/present)
5. ❌ Including irrelevant information
6. ❌ Exceeding one page

### **Formatting Mistakes:**
1. ❌ Bullet points wrapping to 2 lines
2. ❌ Inconsistent spacing between sections
3. ❌ Using multiple font sizes for body text
4. ❌ Special characters showing as "?"
5. ❌ PDF generated with wrong encoding
6. ❌ Headers/footers in PDF

### **Technical Mistakes:**
1. ❌ Using simple PDF generators (lose formatting)
2. ❌ Not testing PDF text extraction
3. ❌ Forgetting to update both .md and .html files
4. ❌ Not verifying company name in final PDF
5. ❌ Skipping the quality checklist

---

## 📝 File Naming Convention

```
Thind, Ranvir - [Company] [Position] Resume.md
Thind, Ranvir - [Company] [Position] Resume.html
Thind, Ranvir - [Company] [Position] Resume.pdf
```

**Examples:**
- `Thind, Ranvir - Alaska Airlines Financial Analyst Resume.pdf`
- `Thind, Ranvir - Microsoft FRP Analyst Resume.pdf`

---

## 🔄 Update Process

When updating resumes:

1. **Update .md file** with content changes
2. **Update .html file** with same changes
3. **Regenerate PDF** using Chrome headless
4. **Verify** using quality checklist
5. **Test** PDF text extraction
6. **Confirm** one page only

---

## 💡 Pro Tips

1. **Tailor for ATS:** Use exact keywords from job description
2. **Quantify everything:** Even estimates are better than no numbers
3. **Show progression:** Demonstrate growth and increasing responsibility
4. **Be specific:** "Automated reporting for 2,000+ accounts" > "Automated reporting"
5. **Use industry terms:** Match the language in the job posting
6. **Keep it scannable:** Recruiters spend 6-7 seconds on first pass
7. **Test readability:** Can someone understand your value in 10 seconds?

---

## 🎓 Resources

- **ATS Testing:** Paste resume text into Jobscan or similar
- **Grammar Check:** Grammarly or LanguageTool
- **PDF Validation:** `pdftotext` to check text extraction
- **Length Check:** `pdfinfo` to verify page count

---

## 📞 Support

If PDF generation fails:
1. Check Chrome is installed: `google-chrome --version`
2. Verify HTML file has UTF-8 encoding
3. Test HTML in browser first
4. Check for syntax errors in HTML
5. Ensure output path is writable

---

**Last Updated:** January 2026
**Version:** 2.0
**Maintained by:** AI Resume Generation System
