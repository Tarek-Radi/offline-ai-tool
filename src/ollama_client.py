from ollama import chat, ResponseError


MODEL_NAME = "qwen3:4b"


def _call_ollama(prompt: str):
    try:
        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            think=False,
            options={
                "temperature": 0.2,
            },
        )

        return response

    except ResponseError as error:
        raise RuntimeError(
            f"Ollama inference failed: {error}"
        ) from error

    except ConnectionError as error:
        raise RuntimeError(
            "Could not connect to Ollama. Make sure Ollama is running."
        ) from error


def generate_response(prompt: str) -> str:
    response = _call_ollama(prompt)

    content = response.message.content

    if "</think>" in content:
        content = content.split("</think>", 1)[1]

    return content.strip()



# if __name__ == "__main__":
#     prompt = "Explain machine learning in one sentence."
#     response = generate_response(prompt)
#     print(response)