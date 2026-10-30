
print("================================")
print("       PYTHON CHATBOT")
print("================================")
print("Bot: Hello! I am your simple chatbot.")
print("Bot: Type 'bye' to end our conversation.")

while True:
    user_message = input("\nYou: ").strip().lower()

    if not user_message:
        print("Bot: Please type something.")
    elif "hello" in user_message or "hi" in user_message:
        print("Bot: Hello! How are you?")
    elif "how are you" in user_message:
        print("Bot: I'm doing well! Thanks for asking.")
    elif "your name" in user_message:
        print("Bot: My name is CodeAlpha Chatbot.")
    elif "help" in user_message:
        print("Bot: You can greet me, ask my name, or say bye.")
    elif "python" in user_message:
        print("Bot: Python is a popular programming language!")
    elif "thank" in user_message:
        print("Bot: You're welcome!")
    elif user_message in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")

print("Chat ended.")
