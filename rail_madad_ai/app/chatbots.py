def handle_chat(message):
    if 'help' in message.lower():
        return 'How can I assist you today?'
    return "I didn't understand that. Can you please clarify?"
