import pdfplumber
import docx


def extract_text(file):
    if file.name.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text


    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text


    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        return ""