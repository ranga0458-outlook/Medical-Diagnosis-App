import re


def extract_symptoms(text: str) -> list[str]:
    symptoms = re.findall(r"\b(headace|fever|nausea|fatigue|pain)\b", text.lower())
    symptoms = list(set(symptoms))
    return symptoms



