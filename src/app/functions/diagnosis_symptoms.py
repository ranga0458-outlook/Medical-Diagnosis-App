from settings import Settings
from openai import OpenAI

client = OpenAI(api_key=Settings().openai_api_key)


def get_diagnosis(symptoms: list[str]) -> str:
    prompt = f"Patient has symptoms : {', '.join(symptoms)}. Suggest possible medical diagnosis. Suggest me a possible cure for the same."

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": "You are a helpful medical assistant."},
            {"role": "user", "content": prompt},
        ],
    )

    print(response.choices)
    return response.choices[0].message.content.strip()
