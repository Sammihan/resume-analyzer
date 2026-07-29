import pdfplumber
import easyocr
import numpy as np
from pdf2image import convert_from_path
import platform

reader = easyocr.Reader(["en"], gpu=False)


def extract_text_from_pdf(pdf_path):

    pages = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                pages.append(page_text)

    return "\n".join(pages)


def extract_text_using_ocr(pdf_path):

    if platform.system() == "Windows":
        images = convert_from_path(
            pdf_path,
            poppler_path=r"C:\Users\sammi\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin",
        )
    else:
        images = convert_from_path(pdf_path)

    full_text = ""

    for image in images:

        image = np.array(image)

        results = reader.readtext(image)

        page_text = " ".join([text for _, text, _ in results])

        full_text += page_text + "\n"

    return full_text


def extract_text(pdf_path):

    text = extract_text_from_pdf(pdf_path)

    if text.strip():
        print("✅ Embedded text found.")
        return text

    print("📄 No embedded text found. Switching to OCR...")

    return extract_text_using_ocr(pdf_path)
