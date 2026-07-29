from parser.pdf_parser import extract_text
from utils.text_cleaner import clean_text
from parser.contact_parser import parse_contact_info
from parser.skills_parser import extract_skills
from parser.education_parser import parse_education


def analyze_resume(pdf_path):
    raw_text = extract_text(pdf_path)
    cleaned_text = clean_text(raw_text)

    resume = {}

    resume.update(parse_contact_info(cleaned_text))

    resume.update(extract_skills(cleaned_text))

    resume["metadata"] = {"raw_text": raw_text, "cleaned_text": cleaned_text}

    return resume
