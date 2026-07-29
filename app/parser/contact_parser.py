import email
import re


def extract_email(text):
    pattern = r"\S+@\S+\.\S+"
    match = re.search(pattern, text)
    if match:
        return match.group()

    return None


def extract_phone(text):
    pattern = r"(\+\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}"
    match = re.search(pattern, text)
    if match:
        return match.group()
    return None


def extract_linkedin(text):
    pattern = r"(https?://)?(www\.)?linkedin\.com/\S+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def extract_github(text):
    pattern = r"(https?://)?(www\.)?github\.com/\S+"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


def parse_contact_info(text):

    return {
        "contact": {
            "email": extract_email(text),
            "phone": extract_phone(text),
            "linkedin": extract_linkedin(text),
            "github": extract_github(text),
        }
    }
