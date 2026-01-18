# 📋 MASTER RESUME TEMPLATE

## 🎯 THE GOLDEN STANDARD (Updated January 2026)

This is the **perfected resume format** based on research into what recruiters and ATS systems prefer. All AI agents MUST follow this template when creating resumes.

---

## 📊 KEY RESEARCH FINDINGS

Based on 2025-2026 resume best practices:

1. **Recruiters spend 6-8 seconds** scanning a resume - visual hierarchy is critical
2. **Job title on first line, dates aligned right** - eyes naturally scan left→right
3. **Company/location on second line** - keeps title prominent, dates visible
4. **Quantifiable achievements** - numbers and percentages stand out
5. **ATS-friendly formatting** - use standard headings, no tables/graphics
6. **One page** - always, unless 10+ years experience

---

## 📐 OPTIMAL HTML TEMPLATE

Copy this exact template and modify only the content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ranvir Singh Thind - Resume</title>
    <style>
        @page {
            size: Letter;
            margin: 0.5in 0.6in;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-size: 10.5pt;
            font-family: Calibri, 'Segoe UI', Arial, sans-serif;
            line-height: 1.35;
            color: #222;
        }
        
        /* === HEADER === */
        .header {
            text-align: center;
            margin-bottom: 8px;
            padding-bottom: 6px;
            border-bottom: 2px solid #1a1a1a;
        }
        h1 {
            font-size: 22pt;
            font-weight: 700;
            color: #111;
            letter-spacing: 0.5px;
            margin-bottom: 4px;
        }
        .contact-line {
            font-size: 10pt;
            color: #333;
        }
        .contact-line a {
            color: #333;
            text-decoration: none;
        }
        .separator {
            margin: 0 6px;
            color: #666;
        }
        
        /* === SECTION HEADERS === */
        h2 {
            font-size: 10.5pt;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: #111;
            border-bottom: 1px solid #333;
            padding-bottom: 2px;
            margin: 10px 0 6px 0;
        }
        
        /* === SUMMARY === */
        .summary {
            font-size: 10.5pt;
            line-height: 1.4;
            color: #222;
            margin-bottom: 2px;
        }
        
        /* === JOB ENTRY - OPTIMIZED FORMAT === */
        .job-entry {
            margin-bottom: 8px;
        }
        .job-line-1 {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 1px;
        }
        .job-title {
            font-weight: 700;
            font-size: 10.5pt;
            color: #111;
        }
        .job-dates {
            font-size: 10pt;
            color: #333;
            white-space: nowrap;
        }
        .job-line-2 {
            font-size: 10pt;
            color: #444;
            margin-bottom: 3px;
        }
        
        /* === BULLET POINTS === */
        ul {
            margin: 0;
            padding-left: 16px;
        }
        li {
            font-size: 10pt;
            line-height: 1.35;
            margin-bottom: 1px;
            color: #222;
        }
        li strong {
            font-weight: 600;
        }
        
        /* === EDUCATION === */
        .edu-entry {
            margin-bottom: 4px;
        }
        .edu-line-1 {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
        }
        .edu-school {
            font-weight: 700;
            font-size: 10.5pt;
            color: #111;
        }
        .edu-location {
            font-size: 10pt;
            color: #333;
        }
        .edu-degree {
            font-size: 10pt;
            color: #222;
            margin-top: 1px;
        }
        .coursework {
            font-size: 9.5pt;
            color: #444;
            font-style: italic;
            margin-top: 2px;
        }
        
        /* === SKILLS === */
        .skills-section {
            font-size: 10pt;
            line-height: 1.45;
        }
        .skill-row {
            margin-bottom: 2px;
        }
        .skill-category {
            font-weight: 700;
            color: #111;
        }
    </style>
</head>
<body>
    <!-- HEADER - Centered, Clean -->
    <div class="header">
        <h1>RANVIR SINGH THIND</h1>
        <p class="contact-line">
            Seattle, WA<span class="separator">•</span>rjkind01@gmail.com<span class="separator">•</span>(206) 771-8870<span class="separator">•</span><a href="https://linkedin.com/in/ranvir-thind">linkedin.com/in/ranvir-thind</a>
        </p>
    </div>

    <!-- SUMMARY -->
    <h2>Professional Summary</h2>
    <p class="summary">[2-4 sentences: Who you are + Key experience + Value you bring]</p>

    <!-- EXPERIENCE -->
    <h2>Professional Experience</h2>
    
    <div class="job-entry">
        <div class="job-line-1">
            <span class="job-title">[Job Title]</span>
            <span class="job-dates">[Start Date] – [End Date]</span>
        </div>
        <div class="job-line-2">[Company Name] | [City, State]</div>
        <ul>
            <li>[Action verb] + [What you did] + [Quantifiable result]</li>
            <li>...</li>
        </ul>
    </div>

    <!-- EDUCATION -->
    <h2>Education</h2>
    <div class="edu-entry">
        <div class="edu-line-1">
            <span class="edu-school">[University Name]</span>
            <span class="edu-location">[City, State]</span>
        </div>
        <div class="edu-degree">[Degree] – [Major] | <strong>GPA: [X.X]</strong> | [Graduation Date]</div>
        <p class="coursework">Relevant Coursework: [Course 1], [Course 2], [Course 3]</p>
    </div>

    <!-- SKILLS -->
    <h2>Technical Skills</h2>
    <div class="skills-section">
        <div class="skill-row"><span class="skill-category">[Category 1]:</span> Skill A, Skill B, Skill C...</div>
        <div class="skill-row"><span class="skill-category">[Category 2]:</span> Skill A, Skill B, Skill C...</div>
    </div>
</body>
</html>
```

---

## 📏 FORMAT SPECIFICATIONS

| Element | Size | Notes |
|---------|------|-------|
| Name | 22pt, bold, ALL CAPS | Centered, with bottom border |
| Contact Info | 10pt | Centered, bullet separators |
| Section Headers | 10.5pt, bold, UPPERCASE | Letter-spacing 1.2px, underline |
| Job Title | 10.5pt, bold | Left-aligned on line 1 |
| Dates | 10pt | Right-aligned on line 1 |
| Company/Location | 10pt | Left-aligned on line 2, muted color |
| Bullet Points | 10pt | 1.35 line-height, tight margins |
| Skills | 10pt | Category bold, skills comma-separated |

---

## 🎨 VISUAL HIERARCHY

```
┌─────────────────────────────────────────────────────────────┐
│                    RANVIR SINGH THIND                       │  ← 22pt, centered, bold
│        Seattle, WA • email • phone • linkedin               │  ← 10pt, centered
├─────────────────────────────────────────────────────────────┤
│ PROFESSIONAL SUMMARY                                        │  ← Section header
│ [2-4 sentences about experience and value]                  │
├─────────────────────────────────────────────────────────────┤
│ PROFESSIONAL EXPERIENCE                                     │
│ Job Title                              June 2024 – Present  │  ← Title LEFT, Dates RIGHT
│ Company Name | City, State                                  │  ← Second line, muted
│ • Bullet point with achievement and metrics                 │
│ • Another accomplishment with numbers                       │
├─────────────────────────────────────────────────────────────┤
│ EDUCATION                                                   │
│ University Name                                 City, State │  ← School LEFT, Location RIGHT
│ Degree – Major | GPA: X.X | Graduation Date                 │
├─────────────────────────────────────────────────────────────┤
│ TECHNICAL SKILLS                                            │
│ Category: Skill, Skill, Skill, Skill, Skill                 │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ QUALITY CHECKLIST

Before generating PDF, verify:

- [ ] **Page count**: Exactly 1 page
- [ ] **Job format**: Title on line 1 (left), dates on line 1 (right), company on line 2
- [ ] **Bullets**: Action verbs, quantifiable results (%, $, numbers)
- [ ] **Line fill**: 85-100% on all lines, no orphans (single words on last line)
- [ ] **Consistency**: Same format for all job entries
- [ ] **ATS-friendly**: Standard headings, no graphics/tables
- [ ] **Font**: Calibri or similar sans-serif

---

## 🔧 PDF GENERATION

```bash
# Navigate to application folder
cd applications/[DATE]_[Company]_[Position]/

# Generate PDF from HTML using headless Chrome
google-chrome --headless --disable-gpu \
  --print-to-pdf="Thind, Ranvir - Resume.pdf" \
  --no-pdf-header-footer \
  "Thind, Ranvir - [Company] [Position] Resume.html"
```

---

## 📝 MARKDOWN FORMAT

For the `.md` file, use this structure:

```markdown
# RANVIR SINGH THIND

**Seattle, WA** • email • phone • [linkedin](url)

---

## PROFESSIONAL SUMMARY

[Summary paragraph]

---

## PROFESSIONAL EXPERIENCE

**Job Title** | Dates  
Company Name | City, State

- Bullet point
- Bullet point

---

## EDUCATION

**University Name** | City, State  
Degree – Major | **GPA: X.X** | Graduation Date

---

## TECHNICAL SKILLS

**Category:** Skill, Skill, Skill  
```

---

## ⚠️ COMMON MISTAKES TO AVOID

1. ❌ Putting company and dates on same line as job title (too crowded)
2. ❌ Orphan words on last line of sections
3. ❌ Generic duties instead of quantified achievements
4. ❌ Using tables or complex layouts (breaks ATS)
5. ❌ Inconsistent formatting between job entries
6. ❌ Exceeding 1 page

---

## 📚 REFERENCE EXAMPLE

See: `applications/2025-12-27_AlaskaAirlines_FinancialAnalyst/Thind, Ranvir - Alaska Airlines Financial Analyst Resume.html`

This is the gold standard that all new resumes should match.
