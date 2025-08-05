tools = [

    {
        "type": "function",
        "function": {
            "name": "textToSpeech",
            "description": "Converts text to speech simply without additional context.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The initial raw query mentioned made by the user"},
                    "voice": {"type": "string", "description": "The voice to be used for TTS"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "contextualTextToSpeech",
            "description": "Converts text to speech with additional context for a richer response.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The initial raw query mentioned made by the user"},
                    "context": {"type": "string", "description": "Additional context to enhance the TTS response"},
                    "voice": {"type": "string", "description": "The voice to be used for TTS"}
                },
                "required": ["query", "context"]
            }
        }
    }
]