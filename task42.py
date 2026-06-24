responses = {
    "hello": "Hi! How can I help you?",
    "bye": "Goodbye!",
    "how are you": "I'm doing well!"
}

while True:
    user = input("You: ").lower()

    if user in responses:
        print("Bot:", responses[user])

    elif user == "exit":
        break

    else:
        print("Bot: Sorry, I don't understand.")