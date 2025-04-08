import os
import requests

def generate_summary(products):
    api_token = os.getenv("HUGGINGFACE_API_TOKEN")
    headers = {
        "Authorization": f"Bearer {'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'}"
    }
    input_text = f"Summarize the following product list: {products}"
    
    response = requests.post(
        "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf",
        headers=headers,
        json={"inputs": input_text}
    )

    if response.status_code != 200:
        print("Error generating summary:", response.status_code, response.json())
        return "Summary unavailable."
    
    return response.json()[0]['generated_text']
