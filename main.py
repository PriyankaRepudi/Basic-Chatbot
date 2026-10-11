def get_reply(message):
    """Return a predefined reply for a simple user message."""
    message = message.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi! How can I help you?"
    elif message in ("how are you", "how are you?"):
        return "I'm fine, thanks! How are you?"
    elif message in ("what is your name", "what is your name?"):
        return "I'm PyBot, a simple Python chatbot."
    elif message in ("help",):
        return "You can say hello, ask how I am, ask my name, or say bye."
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see what I can answer."


def main():
    print("=== PyBot: Basic Chatbot ===")
    print("Type 'help' for examples or 'bye' to exit.")

    while True:
        user_message = input("You: ")
        reply = get_reply(user_message)
        print("PyBot:", reply)

        if user_message.strip().lower() in ("bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()
