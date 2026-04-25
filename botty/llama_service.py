from settings import LLAMA_CLOUD_API_KEY


def call_llama_api(text):
    api_key = read_secret_key()
    client = connect_to_llama(api_key)

    response = client.ask(text)

    answer = response.text

    return answer





def ask_llama(text):
    if not (text):
        return "please send messagui"

    response = call_llama_api(text)

    return response
