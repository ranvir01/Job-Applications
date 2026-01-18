import sys

def escape_pdf_text(text):
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

def parse_inline_styles(text, base_font_size=11):
    # Returns a string of PDF commands to render the text with formatting
    # Supports **bold** and *italic*
    # Default font F1 (Helvetica), Bold F2, Italic F3
    
    # We will split by ** first
    parts = text.split('**')
    commands = []
    
    for i, part in enumerate(parts):
        is_bold = (i % 2 == 1)
        
        # Now split by * for italics within this part
        subparts = part.split('*')
        for j, subpart in enumerate(subparts):
            if not subpart: continue
            
            is_italic = (j % 2 == 1)
            
            font = "/F1"
            if is_bold and is_italic:
                font = "/F4" # Bold Italic (if we define it, otherwise Bold)
            elif is_bold:
                font = "/F2"
            elif is_italic:
                font = "/F3"
            
            escaped_text = escape_pdf_text(subpart)
            commands.append(f"{font} {base_font_size} Tf ({escaped_text}) Tj")
            
    return " ".join(commands)

def create_advanced_pdf(md_file, pdf_file):
    with open(md_file, 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    content_stream = []
    
    # Page setup
    page_height = 792
    page_width = 612
    margin_left = 50
    margin_top = 750
    margin_right = 50
    
    current_y = margin_top
    
    def add_line(cmds):
        content_stream.append(cmds)
        
    def check_page_break(y_pos, needed_space):
        # If we are too low, simple page break logic could go here
        # But for 1 page resume we just assume it fits or warn
        return y_pos

    # Iterate lines
    skip_until_content = False
    for line in lines:
        if not line:
            current_y -= 6 # Small paragraph gap
            continue
        
        # Skip frontmatter (between --- markers)
        if line.startswith('---'):
            skip_until_content = not skip_until_content
            continue
        if skip_until_content:
            continue
            
        # Skip CSS/style blocks
        if line.startswith('<style') or line.startswith('</style>') or line.startswith('pdf_options') or line.startswith('format:') or line.startswith('margin:'):
            continue
        if line.startswith('body {') or line.startswith('h1 {') or line.startswith('h2 {') or line.startswith('p {') or line.startswith('li {') or line.startswith('ul {') or line.startswith('hr {') or line.startswith('strong {') or line.startswith('em {') or line.startswith('a {'):
            continue
            
        # Header (Name)
        if line.startswith('# '):
            name = line[2:]
            # Centered or Left? McKinsey example is Left aligned title, but let's stick to standard Left
            # Actually user resume usually centered? The HTML showed H1 left aligned (implied by no text-align:center)
            # Let's do Left aligned 24pt Bold
            current_y -= 10
            add_line(f"BT /F2 22 Tf {margin_left} {current_y} Td ({escape_pdf_text(name)}) Tj ET")
            current_y -= 30
            
        # Section Header
        elif line.startswith('## '):
            section = line[3:].upper()
            current_y -= 10
            # Draw line
            # Line width 1, black
            add_line(f"1 w 0 g {margin_left} {current_y-2} m {page_width-margin_right} {current_y-2} l S")
            # Text
            add_line(f"BT /F2 11 Tf {margin_left} {current_y} Td ({escape_pdf_text(section)}) Tj ET")
            current_y -= 16
            
        # Bullet Points
        elif line.startswith('- '):
            content = line[2:]
            # Draw bullet
            bullet_y = current_y
            add_line(f"BT /F1 11 Tf {margin_left+10} {bullet_y} Td (•) Tj ET")
            
            # Draw text
            # We assume text fits on one line as requested
            text_cmds = parse_inline_styles(content, 11)
            add_line(f"BT {margin_left+25} {bullet_y} Td {text_cmds} ET")
            
            current_y -= 14 # Line height
            
        # Contact Info Line (special detection)
        elif '|' in line and '@' in line:
            # Remove MD bold markers if any for the whole line, or parse them
            # Center this? The HTML had it left. Let's do Left.
            # It usually has links, we just render text.
            # Clean up [link](url) format
            import re
            clean_line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)
            
            text_cmds = parse_inline_styles(clean_line, 10)
            add_line(f"BT {margin_left} {current_y} Td {text_cmds} ET")
            current_y -= 16
            
        # Normal Text (Summary, etc)
        else:
            # Check for key: value pairs (Skills)
            if ':' in line and len(line) < 200:
                # Skill line
                text_cmds = parse_inline_styles(line, 11)
                add_line(f"BT {margin_left} {current_y} Td {text_cmds} ET")
                current_y -= 14
            else:
                # Regular paragraph text (Summary)
                # Need simple wrapping if long
                words = line.split(' ')
                current_line = []
                line_len = 0
                max_len = 90 # Approx chars per line
                
                for word in words:
                    # Strip md links
                    word = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', word)
                    
                    if line_len + len(word) > max_len:
                        # Flush line
                        full_line = " ".join(current_line)
                        text_cmds = parse_inline_styles(full_line, 11)
                        add_line(f"BT {margin_left} {current_y} Td {text_cmds} ET")
                        current_y -= 14
                        current_line = [word]
                        line_len = len(word)
                    else:
                        current_line.append(word)
                        line_len += len(word) + 1
                
                # Flush last line
                if current_line:
                    full_line = " ".join(current_line)
                    text_cmds = parse_inline_styles(full_line, 11)
                    add_line(f"BT {margin_left} {current_y} Td {text_cmds} ET")
                    current_y -= 14

    # Build PDF Objects
    objects = []
    
    # Obj 1: Helvetica (F1)
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    # Obj 2: Helvetica-Bold (F2)
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    # Obj 3: Helvetica-Oblique (F3)
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique >>")
    # Obj 4: Helvetica-BoldOblique (F4)
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-BoldOblique >>")
    
    # Obj 5: Font Resources Dict (to reference F1-F4)
    font_res = b"<< /F1 1 0 R /F2 2 0 R /F3 3 0 R /F4 4 0 R >>"
    objects.append(font_res)

    # Obj 6: Content Stream
    stream_data = "\n".join(content_stream).encode('latin-1', errors='replace')
    objects.append(b"<< /Length " + str(len(stream_data)).encode('ascii') + b" >>\nstream\n" + stream_data + b"\nendstream")
    
    # Obj 7: Page
    # Resources point to Obj 5
    objects.append(b"<< /Type /Page /Parent 8 0 R /Resources << /Font 5 0 R >> /MediaBox [0 0 612 792] /Contents 6 0 R >>")
    
    # Obj 8: Pages
    objects.append(b"<< /Type /Pages /Kids [7 0 R] /Count 1 >>")
    
    # Obj 9: Catalog
    objects.append(b"<< /Type /Catalog /Pages 8 0 R >>")
    
    # Write File
    with open(pdf_file, 'wb') as f:
        f.write(b"%PDF-1.4\n")
        offsets = []
        
        for i, obj_data in enumerate(objects):
            oid = i + 1
            offsets.append(f.tell())
            f.write(f"{oid} 0 obj\n".encode('ascii'))
            f.write(obj_data)
            f.write(b"\nendobj\n")
            
        xref_start = f.tell()
        f.write(b"xref\n")
        f.write(f"0 {len(objects) + 1}\n".encode('ascii'))
        f.write(b"0000000000 65535 f \n")
        for off in offsets:
            f.write(f"{off:010d} 00000 n \n".encode('ascii'))
            
        f.write(b"trailer\n")
        f.write(f"<< /Size {len(objects) + 1} /Root 9 0 R >>\n".encode('ascii'))
        f.write(b"startxref\n")
        f.write(f"{xref_start}\n".encode('ascii'))
        f.write(b"%%EOF\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        create_advanced_pdf(sys.argv[1], sys.argv[2])
    else:
        create_advanced_pdf("Thind, Ranvir- Resume.md", "Thind, Ranvir- Resume.pdf")
