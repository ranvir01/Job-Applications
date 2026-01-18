import re

class SimplePDF:
    def __init__(self):
        self.objects = []
        self.offsets = []
        self.buffer = bytearray()
        self.write(b"%PDF-1.4\n")

    def write(self, data):
        self.buffer.extend(data)

    def add_object(self, obj_id, content):
        offset = len(self.buffer)
        self.offsets.append((obj_id, offset))
        self.write(f"{obj_id} 0 obj\n".encode('latin-1'))
        self.write(content)
        self.write(b"\nendobj\n")

    def save(self, filename):
        # Font (Obj 1)
        self.add_object(1, b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

        # Page Content (Obj 2) is added later
        
        # Page (Obj 3)
        self.add_object(3, b"<< /Type /Page /Parent 4 0 R /Resources << /Font << /F1 1 0 R /F2 1 0 R >> >> /MediaBox [0 0 612 792] /Contents 2 0 R >>")
        
        # Pages (Obj 4)
        self.add_object(4, b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
        
        # Catalog (Obj 5)
        self.add_object(5, b"<< /Type /Catalog /Pages 4 0 R >>")

        # XRef
        xref_offset = len(self.buffer)
        self.write(b"xref\n")
        self.write(f"0 {len(self.objects) + 1}\n".encode('latin-1'))
        self.write(b"0000000000 65535 f \n")
        
        # Sort offsets by ID to ensure correct order in xref if we added them out of order (we didn't, but good practice)
        # Actually standard requires objects to be distinct. My add_object just appends.
        # But wait, I need to add Obj 2 (content) before I can calculate its length.
        # So I need to structure this better.
        pass

def create_pdf(md_file, pdf_file):
    with open(md_file, 'r') as f:
        lines = f.readlines()

    # Prepare content stream
    content_cmds = []
    y = 750
    
    # Font setup
    # F1: Helvetica (Body)
    # F2: Helvetica-Bold (Headers)
    
    def add_text(text, font, size, x, y):
        # Escape parenthesis and backslashes
        text = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
        return f"BT /{font} {size} Tf {x} {y} Td ({text}) Tj ET"

    for line in lines:
        line = line.strip()
        if not line: continue
        if line.startswith('---') or line.startswith('<style') or line.startswith('body {') or line.startswith('h1 {') or line.startswith('h2 {') or line.startswith('p {') or line.startswith('li {') or line.startswith('ul {') or line.startswith('hr {') or line.startswith('strong {') or line.startswith('em {') or line.startswith('a {') or line.startswith('</style>'):
             continue
        if line.startswith('pdf_options:'): continue
        if line.startswith('format:'): continue
        if line.startswith('margin:'): continue

        if line.startswith('# '):
            # Title
            content_cmds.append(add_text(line[2:], "F1", 18, 50, y))
            y -= 25
        elif line.startswith('## '):
            # Section
            y -= 10
            content_cmds.append(add_text(line[3:].upper(), "F1", 12, 50, y)) # Using F1 for bold effect by size or just F1? Standard 14 fonts include Bold.
            # I only defined Helvetica. Let's assume F1 is Helvetica. To get Bold I need another font object.
            # For simplicity, I'll use F1 for everything but size changes.
            y -= 15
        elif line.startswith('**') and '|' in line:
            # Contact info line
            # Remove MD formatting roughly
            text = line.replace('**', '').replace('[', '').replace(']', '').split('(')[0] # clean link
            content_cmds.append(add_text(text, "F1", 10, 50, y))
            y -= 20
        elif line.startswith('**') and 'Present' in line:
             # Job Header
             text = line.replace('**', '')
             content_cmds.append(add_text(text, "F1", 11, 50, y))
             y -= 15
        elif line.startswith('- '):
            # Bullet
            text = line[2:].replace('**', '')
            # Simple wrapping? No, assuming 1 line as requested.
            content_cmds.append(add_text("• " + text, "F1", 10, 60, y))
            y -= 12
        else:
            # Normal text
            text = line.replace('**', '')
            # If text is long, simple split?
            if len(text) > 90:
                parts = []
                while len(text) > 90:
                    idx = text.rfind(' ', 0, 90)
                    if idx == -1: idx = 90
                    parts.append(text[:idx])
                    text = text[idx+1:]
                parts.append(text)
                for p in parts:
                    content_cmds.append(add_text(p, "F1", 10, 50, y))
                    y -= 12
            else:
                content_cmds.append(add_text(text, "F1", 10, 50, y))
                y -= 14

    content_stream = '\n'.join(content_cmds).encode('latin-1', errors='replace')
    
    # Build PDF file
    objects = []
    
    # 1: Font Helvetica
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    
    # 2: Content Stream
    objects.append(b"<< /Length " + str(len(content_stream)).encode('latin-1') + b" >>\nstream\n" + content_stream + b"\nendstream")
    
    # 3: Page
    objects.append(b"<< /Type /Page /Parent 4 0 R /Resources << /Font << /F1 1 0 R >> >> /MediaBox [0 0 612 792] /Contents 2 0 R >>")
    
    # 4: Pages
    objects.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
    
    # 5: Catalog
    objects.append(b"<< /Type /Catalog /Pages 4 0 R >>")
    
    with open(pdf_file, 'wb') as f:
        f.write(b"%PDF-1.4\n")
        offsets = []
        
        for i, obj_content in enumerate(objects):
            oid = i + 1
            offsets.append(f.tell())
            f.write(f"{oid} 0 obj\n".encode('latin-1'))
            f.write(obj_content)
            f.write(b"\nendobj\n")
            
        xref_start = f.tell()
        f.write(b"xref\n")
        f.write(f"0 {len(objects) + 1}\n".encode('latin-1'))
        f.write(b"0000000000 65535 f \n")
        for off in offsets:
            f.write(f"{off:010d} 00000 n \n".encode('latin-1'))
            
        f.write(b"trailer\n")
        f.write(f"<< /Size {len(objects) + 1} /Root 5 0 R >>\n".encode('latin-1'))
        f.write(b"startxref\n")
        f.write(f"{xref_start}\n".encode('latin-1'))
        f.write(b"%%EOF\n")

if __name__ == '__main__':
    import sys
    if len(sys.argv) >= 3:
        create_pdf(sys.argv[1], sys.argv[2])
    else:
        create_pdf('Thind, Ranvir- Resume.md', 'Thind, Ranvir- Resume.pdf')
