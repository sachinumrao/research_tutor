import pdfplumber


def clean_page_text(text):
    # after removing non digits from a line, if length is less than 4 discard the line
    
    lines = text.split("\n")
    cln_lines = []
    for l in lines:
        l_ = ''.join(filter(lambda x: x.isalpha() or x.isspace(), l))
        if len(l_) > 4:
            cln_lines.append(l)
    
    cln_text = "\n".join(cln_lines)
    return cln_text


def read_pdf(pdf_path, n_pages=1):
    """Reads a pdf from given path and returns list of pages"""
    print(f"Parsing pdf: {pdf_path}")
    pdf_content = []
    with pdfplumber.open(pdf_path) as pdf:
        pdf_content = [p.extract_text_simple(x_tolerance=1, y_tolerance=1) for idx, p in enumerate(pdf.pages) if idx < n_pages]
           
    print(f"Pages found: {len(pdf_content)}")
    return pdf_content


def parse_pdf(pdf_path, n_pages=1):
    """Parses content of a pdf into a text string"""

    # read pdf
    pdf_content = read_pdf(pdf_path, n_pages=n_pages)
    # print(type(pdf_pages))
    # print(len(pdf_pages))
    
   
    # join content together
    clean_text = [clean_page_text(t) for t in pdf_content]
    
    txt_file = pdf_path.replace(".pdf", ".txt")
    with open(txt_file, "w") as f:
        for item in clean_text:
            f.write(item)
            f.write("\n")
            
    print(f"Output successfully written to {txt_file}...")


if __name__ == "__main__":
    pdf_path = "./../assets/attention_paper.pdf"
    parse_pdf(pdf_path, n_pages=10)