def format_conversation(messages):
    prompt = ""
    for message in messages:
        if message["role"] == "user":
            prompt += f"User: {message['content']}\n"
        else:
            prompt += f"Assistant: {message['content']}\n"
    return prompt