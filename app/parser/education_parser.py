from utils.degree_db import DEGREES


def extract_degree(text):

    lower_text = text.lower()

    for degree in DEGREES:
        if degree.lower() in lower_text:
            return degree

    return None


import re


def extract_cgpa(text):

    pattern = r"\b\d\.\d{1,2}\b"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_years(text):

    pattern = r"20\d{2}\s*[--]\s*20\d{2}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def parse_education(text):

    return {
        "degree": extract_degree(text),
        "cgpa": extract_cgpa(text),
        "years": extract_years(text),
    }
