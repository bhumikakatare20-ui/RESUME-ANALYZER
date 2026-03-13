import PyPDF2

def extract_text(file):
    text = ""

    try:
        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    except:
        text = "error"

    return text.lower()