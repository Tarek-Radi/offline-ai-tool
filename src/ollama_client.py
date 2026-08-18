from ollama import chat


MODEL_NAME = "qwen3:4b"


def generate_response(prompt: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )

    return response.message.content


if __name__ == "__main__":
    prompt = "Explain machine learning in one sentence."
    response = generate_response(prompt)
    print(response)