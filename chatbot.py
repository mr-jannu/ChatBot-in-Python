print("AI Chatbot Started!")
print("Type 'bye' to stop.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")
    
    elif user == "how are you":
        print("Bot: I am fine!")

    elif user == "what is your name":
        print("Bot: I am AI Chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")