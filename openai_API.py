import openai


class OpenAI_API:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def generate_text(self, message):
        prompt = message.text
        model_engine = "text-davinci-002"  # The GPT model to use for text generation
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text
