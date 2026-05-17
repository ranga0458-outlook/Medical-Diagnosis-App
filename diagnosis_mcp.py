from mcp.server.fastmcp import FastMCP

from functions.diagnosis_symptoms import *
from functions.symptom_extractor import *
from functions.pubmed_articles import *
from functions.summarize_pubmed import *

mcp = FastMCP("Clinical Insight AI")

@mcp.tool()
async def clinical_insight_ai(symptom_text):
    # using regular expression to get the symptoms
    symptoms = extract_symptoms(text=symptom_text)

    # send these symptoms to AI to get the result
    diagnosis_result = get_diagnosis(symptoms)

    # get the related articles from pub-med
    pubmed_articles = fetch_pubmed_articles_with_metadata(" ".join(symptoms))

    # summarize the articles as it contains comprehensive result
    summary = summarize_text(pubmed_articles[:3000])

    return {"symptom": symptoms, "diagnosis": diagnosis_result, "pubmed_summary": summary}


if __name__ == "__main__":
    mcp.run(transport="stdio")
