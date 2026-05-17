from settings import Settings
from openai import OpenAI

client = OpenAI(api_key=Settings().openai_api_key)


def summarize_text(text: list[str]) -> str:
    prompt = f"Summarize the following medical abstract:\n\n {text}"

    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role": "system", "content": "You are a helpful medical research summarizer."},
            {"role": "user", "content": prompt},
        ],
    )

    print(response.choices)
    return response.choices[0].message.content.strip()
