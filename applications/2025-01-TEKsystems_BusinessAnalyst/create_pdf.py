#!/usr/bin/env python3
"""
Simple PDF generator for resume using raw PDF format
"""

def create_simple_pdf(content, output_file):
    """Create a basic PDF with the resume content"""

    # PDF header
    pdf_content = b"%PDF-1.4\n"

    # Font object
    font_obj = b"""1 0 obj
<<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
>>
endobj
"""

    # Content stream with the resume text
    # Split content into lines and format for PDF
    lines = content.split('\n')
    formatted_lines = []
    y_position = 750  # Start near top of page

    for line in lines:
        if line.strip():
            if line.startswith('# '):
                # Header
                formatted_lines.append(f"BT /F1 14 Tf 50 {y_position} Td ({line[2:].strip()}) Tj ET")
                y_position -= 20
            elif line.startswith('## '):
                # Subheader
                formatted_lines.append(f"BT /F1 12 Tf 50 {y_position} Td ({line[3:].strip()}) Tj ET")
                y_position -= 18
            elif line.startswith('### '):
                # Sub-subheader
                formatted_lines.append(f"BT /F1 11 Tf 50 {y_position} Td ({line[4:].strip()}) Tj ET")
                y_position -= 16
            elif line.startswith('- '):
                # Bullet point
                formatted_lines.append(f"BT /F1 10 Tf 70 {y_position} Td ({line[2:].strip()}) Tj ET")
                y_position -= 14
            elif '**' in line and '**' in line:
                # Bold text
                parts = line.split('**')
                if len(parts) >= 3:
                    formatted_lines.append(f"BT /F1 10 Tf 50 {y_position} Td ({parts[0]}{parts[1]}{parts[2]}) Tj ET")
                else:
                    formatted_lines.append(f"BT /F1 10 Tf 50 {y_position} Td ({line.strip()}) Tj ET")
                y_position -= 14
            else:
                # Regular text
                formatted_lines.append(f"BT /F1 10 Tf 50 {y_position} Td ({line.strip()}) Tj ET")
                y_position -= 12

            # Reset to new page if needed
            if y_position < 50:
                y_position = 750

    content_stream = '\n'.join(formatted_lines)

    # Page content object
    page_content = f"""2 0 obj
<<
/Length {len(content_stream.encode('utf-8'))}
>>
stream
{content_stream}
endstream
endobj
"""

    # Page object
    page_obj = b"""3 0 obj
<<
/Type /Page
/Parent 4 0 R
/Resources <<
/Font <<
/F1 1 0 R
>>
>>
/MediaBox [0 0 612 792]
/Contents 2 0 R
>>
endobj
"""

    # Pages object
    pages_obj = b"""4 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj
"""

    # Catalog object
    catalog_obj = b"""5 0 obj
<<
/Type /Catalog
/Pages 4 0 R
>>
endobj
"""

    # XRef table
    xref_table = b"""xref
0 6
0000000000 65535 f
0000000009 00000 n
0000000058 00000 n
0000000XXX 00000 n
0000000YYY 00000 n
0000000ZZZ 00000 n
"""

    # Trailer
    trailer = b"""trailer
<<
/Size 6
/Root 5 0 R
>>
startxref
XXX
%%EOF
"""

    # Write the PDF
    with open(output_file, 'wb') as f:
        f.write(pdf_content)
        f.write(font_obj)
        f.write(page_content.encode('utf-8'))
        f.write(page_obj)
        f.write(pages_obj)
        f.write(catalog_obj)
        f.write(xref_table)
        f.write(trailer)

    print(f"PDF created: {output_file}")

if __name__ == "__main__":
    # Read the markdown content
    with open('/home/naan/projects/Job-Applications/applications/2025-01-TEKsystems_BusinessAnalyst/Thind_Ranvir_TEKsystems_Resume.md', 'r') as f:
        content = f.read()

    create_simple_pdf(content, '/home/naan/projects/Job-Applications/applications/2025-01-TEKsystems_BusinessAnalyst/Thind_Ranvir_TEKsystems_Resume.pdf')