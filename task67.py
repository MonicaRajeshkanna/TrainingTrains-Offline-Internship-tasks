def chatbot(message):

    if message.lower()=="hello":
        return "Hi!"

    elif message.lower()=="bye":
        return "Goodbye!"

    else:
        return "I don't understand."

while True:

    msg=input("You: ")

    if msg=="exit":
        break

    print(chatbot(msg))