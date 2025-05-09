import pdfplumber
import re
import os

def pdf_to_markdown(pdf_path, output_path=None):
    """
    Convert a PDF file to markdown format
    
    Args:
        pdf_path: Path to the PDF file
        output_path: Path to save the markdown file, if None, will use the same name as PDF but with .md extension
    
    Returns:
        The path to the created markdown file
    """
    if output_path is None:
        base_name = os.path.splitext(pdf_path)[0]
        output_path = f"{base_name}.md"
    
    print(f"Converting {pdf_path} to {output_path}")
    
    with pdfplumber.open(pdf_path) as pdf:
        all_text = []
        
        # Process each page
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                # Basic formatting improvements
                # 1. Detect headers (assuming headers are shorter lines that don't end with punctuation)
                lines = text.split('\n')
                formatted_lines = []
                
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Check if this looks like a header
                    if len(line) < 100 and not re.search(r'[.,:;!?]$', line) and line[0].isalnum():
                        # Detect heading level based on indentation or other patterns
                        if re.match(r'^[一二三四五六七八九十]+、', line) or re.match(r'^[0-9]+\.[0-9]+', line):
                            formatted_lines.append(f"## {line}")
                        elif re.match(r'^[0-9]+\.', line) or re.match(r'^[（(][0-9]+[）)]', line):
                            formatted_lines.append(f"### {line}")
                        else:
                            # Add as normal text
                            formatted_lines.append(line)
                    else:
                        # Regular paragraph text
                        formatted_lines.append(line)
                
                all_text.extend(formatted_lines)
                all_text.append("\n---\n")  # Page separator
    
    # Write to markdown file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# 血液净化标准操作规程（2021版）\n\n")
        f.write("\n\n".join(all_text))
    
    print(f"Conversion complete. Markdown saved to {output_path}")
    return output_path

if __name__ == "__main__":
    # Path to the PDF file
    pdf_path = "血液净化标准操作规程（2021版）.pdf"
    
    # Convert to markdown
    output_path = pdf_to_markdown(pdf_path)
    print(f"Created markdown file: {output_path}") 