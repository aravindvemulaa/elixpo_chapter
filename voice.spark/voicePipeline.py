import requests
import os
from tools import tools

POLLINATIONS_ENDPOINT = "https://text.pollinations.ai/openai"
MODEL = "openai-fast"
TOKEN = os.getenv("TOKEN")
REFERRER = os.getenv("REFERRER")

def build_system_prompt():
    return """
        You are a voice actor, and you have two major tasks, one is to either 
        generate a TTS response that is directly generate the speech from the user query
        or to generate a TTS response that is a follow-up question to the user query or has 
        a contextual follow-up question to the user query.

        If you feel the user is straightforward and is not of any context or background then simply
        generate a TTS response that is directly related to the user query.

        if you feel like the user is asking a voice over to a specific context or background then
        generate a TTS response that is a follow-up question to the user query or has a
        contextual follow-up question to the user query.

        The tools you have are 
        - textToSpeech(query): used if the user directly asks for a TTS response without any context.
        - contextualTextToSpeech(query, context): used if the user asks for a TTS response with 
        additional context.

        You should use these tools to generate the TTS response based on the user's query.
        For a direct TTS, do not include any additional context, just the user prompt to the voice!
        For a contextual TTS, include the context to enhance the response with voice acting.
        """


def generate_tts(user_query: str):
    system_prompt = build_system_prompt()
    headers = {"Content-Type": "application/json"}
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]
    payload = {
        "model": MODEL,
        "messages": messages,
        "tools": tools,
        "tool_choice": "auto",
        "token": TOKEN,
        "referrer": REFERRER,
        "temperature": 0.2,
        "private": True
    }
    try:
        response = requests.post(POLLINATIONS_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Pollinations API call failed at iteration  {e}")

    assistant_message = response_data["choices"][0]["message"]
    tool_calls = assistant_message.get("tool_calls")
    return tool_calls

if __name__ == "__main__":
    query = "Convert to speech --> 'What is the capital of France?'"
    result = generate_tts(query)
    if result:
        print("Generated TTS content:", result)
    else:
        print("No TTS content generated.")