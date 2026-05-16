from functions.diagnosis_symptoms import *
from functions.symptom_extractor import *
from functions.pubmed_articles import *


def main():
    print("Hello from medical-diagnosis-app!")

    symptoms = extract_symptoms(text="I have a headache and fever, but no nausea or fatigue")
    get_diagnosis(symptoms)

    fetch_pubmed_articles_with_metadata("back pain")


if __name__ == "__main__":
    main()
