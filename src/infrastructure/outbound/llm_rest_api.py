from openai import OpenAI

client = OpenAI(
    base_url="http://192.168.1.154:1234/v1",
    api_key="lm-studio"  # could be any string
)

MODEL_NAME = ""  # Can be emtpy if there's only one model loaded

def message(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500
    )

    msg = response.choices[0].message
    if not msg or not msg.content:
        raise Exception("Error: No content in the response message.")

    return msg.content