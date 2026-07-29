from parser.pdf_parser import extract_text
from parser.skills_parser import extract_skills
from utils.text_cleaner import clean_text


def analyze_job_description(pdf_path):

    raw_text = extract_text(pdf_path)

    cleaned_text = clean_text(raw_text)

    job = {}

    job.update(extract_skills(cleaned_text))

    job["metadata"] = {"raw_text": raw_text, "cleaned_text": cleaned_text}

    return job
