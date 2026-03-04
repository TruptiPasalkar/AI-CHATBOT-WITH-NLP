import nltk
from nltk.tokenize import word_tokenize

print("🤖 Chatbot is running! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye! 👋")
        break

    tokens = word_tokenize(user_input)

    if "hello" in tokens or "hi" in tokens:
        print("Bot: Hello! How can I help you?")

    elif "weather" in tokens:
        print("Bot: I can tell weather if you connect me to an API 😉")

    elif "name" in tokens:
        print("Bot: I am your internship chatbot!")

    elif "bye" in tokens:
        print("Bot: See you soon!")

    else:
        print("Bot: Sorry, I don't understand that yet.")