#!/usr/bin/env python3

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import inch

def create_resume_pdf():
    doc = SimpleDocTemplate("Thind, Ranvir- Resume.pdf", pagesize=letter,
                           rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=12,
        alignment=1  # Center alignment
    )

    header_style = ParagraphStyle(
        'Header',
        parent=styles['Normal'],
        fontSize=10,
        alignment=1,  # Center alignment
        spaceAfter=20
    )

    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        borderWidth=0,
        borderPadding=0
    )

    job_style = ParagraphStyle(
        'Job',
        parent=styles['Normal'],
        fontSize=12,
        fontName='Helvetica-Bold',
        spaceAfter=6
    )

    details_style = ParagraphStyle(
        'Details',
        parent=styles['Normal'],
        fontSize=10,
        textColor='gray',
        spaceAfter=10
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=20,
        spaceAfter=6
    )

    story = []

    # Header
    story.append(Paragraph("Ranvir Singh Thind", title_style))
    story.append(Paragraph("Seattle, WA | rjkind01@gmail.com | (206) 771-8870 | linkedin.com/in/ranvir-thind", header_style))
    story.append(Spacer(1, 12))

    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    summary_text = """Analytical problem-solver with 4 years of experience in business analysis, financial modeling, and strategic consulting. Proven ability to structure complex problems, analyze data-driven insights, and deliver actionable recommendations. Strong communicator skilled at creating compelling presentations and collaborating cross-functionally. Experience managing independent projects, meeting tight deadlines, and adapting to dynamic environments."""
    story.append(Paragraph(summary_text, styles['Normal']))
    story.append(Spacer(1, 20))

    # Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))

    # Job 1
    story.append(Paragraph("Business Analyst & Consultant | MyConsulting Network | Seattle, WA | June 2024 – Present", job_style))
    bullets1 = [
        "Led engagements solving complex business challenges through structured problem-solving and data analysis",
        "Developed comprehensive business cases and financial models to support strategic recommendations, achieving 15-20% performance improvements",
        "Conducted stakeholder interviews and workshops to identify root causes and develop collaborative solutions",
        "Created professional deliverables including presentations, Excel models, and implementation plans",
        "Managed multiple concurrent projects independently, balancing priorities and meeting deadlines",
        "Automated reporting processes for 2,000+ accounts, improving efficiency by 30% through data analysis and process optimization"
    ]
    for bullet in bullets1:
        story.append(Paragraph(f"• {bullet}", bullet_style))

    story.append(Spacer(1, 12))

    # Job 2
    story.append(Paragraph("Business Manager & Analyst | Thind Transport LLC | Kent, WA | June 2020 – June 2024", job_style))
    bullets2 = [
        "Managed $500K+ annual operations through analytical decision-making and performance tracking",
        "Collaborated with operations and accounting teams to streamline processes and reduce costs by 10%",
        "Developed financial models and variance analyses to inform data-driven business decisions",
        "Created executive presentations and reports to communicate complex financial data to diverse audiences",
        "Led month-end close processes, ensuring accuracy and compliance through systematic reconciliation",
        "Managed vendor relationships and contract negotiations, demonstrating strong organizational skills"
    ]
    for bullet in bullets2:
        story.append(Paragraph(f"• {bullet}", bullet_style))

    story.append(Spacer(1, 20))

    # Education
    story.append(Paragraph("EDUCATION", section_style))
    education_text = """<b>University of Washington – Michael G. Foster School of Business | Seattle, WA</b><br/>
Bachelor of Arts in Business Administration – Finance | GPA: 3.6 | Graduated Spring 2024<br/>
<i>Relevant Coursework:</i> Business Analytics, Managerial Accounting, Corporate Finance, Operations Management, Strategic Management"""
    story.append(Paragraph(education_text, styles['Normal']))
    story.append(Spacer(1, 20))

    # Technical & Analytical Skills
    story.append(Paragraph("TECHNICAL & ANALYTICAL SKILLS", section_style))

    skills_data = [
        ("Data Analysis & Modeling:", "Excel (advanced modeling, VBA automation, pivot tables), SQL, Tableau, financial forecasting"),
        ("Communication & Presentation:", "PowerPoint, stakeholder presentations, professional deliverables, workshop facilitation"),
        ("Problem-Solving Frameworks:", "Root cause analysis, hypothesis testing, scenario planning, decision-tree modeling"),
        ("Project Management:", "Independent execution, time management, cross-functional collaboration, deadline-driven delivery"),
        ("Industry Knowledge:", "Operations optimization, financial analysis, process improvement, strategic planning")
    ]

    for category, skills in skills_data:
        story.append(Paragraph(f"<b>{category}</b> {skills}", styles['Normal']))
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 20))

    # Additional Qualifications
    story.append(Paragraph("ADDITIONAL QUALIFICATIONS", section_style))
    quals = [
        "<b>Travel & Flexibility:</b> Willing to work extended hours and adapt to dynamic project needs",
        "<b>Languages:</b> English (native), willing to learn additional languages as needed",
        "<b>Commitment to Impact:</b> Dedicated to driving meaningful change through analytical rigor and collaborative problem-solving"
    ]
    for qual in quals:
        story.append(Paragraph(f"• {qual}", bullet_style))

    doc.build(story)
    print("PDF resume created successfully: Thind, Ranvir- Resume.pdf")

if __name__ == "__main__":
    create_resume_pdf()