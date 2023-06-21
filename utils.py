import openai


def is_openai_api_correct(openai_api_key):
    try:
        openai.api_key = openai_api_key
        models = openai.Model.list()
        return True
    except Exception:
        return False
