import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from functions.diagnosis_symptoms import *
from functions.symptom_extractor import *
from functions.pubmed_articles import *
from functions.summarize_pubmed import *

app = FastAPI()


class SymptomInput(BaseModel):
    description: str


@app.post("/diagnosis")
def diagnosis(symptominput: SymptomInput):
    # using regular expression to get the symptoms
    symptoms = extract_symptoms(text=symptominput.description)

    # send these symptoms to AI to get the result
    diagnosis_result = get_diagnosis(symptoms)

    # get the related articles from pub-med
    pubmed_articles = fetch_pubmed_articles_with_metadata(" ".join(symptoms))

    # summarize the articles as it contains comprehensive result
    summary = summarize_text(pubmed_articles[:3000])

    return {"symptom": symptoms, "diagnosis": diagnosis_result, "pubmed_summary": summary}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
