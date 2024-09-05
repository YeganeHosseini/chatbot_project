import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Simple rule-based responses
    if re.search(r'hi|hello', user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r'how are you', user_input):
        return "I'm just a bot, but I'm doing well! How about you?"
    elif re.search(r'what is your name', user_input):
        return "I'm Chemnibo, your assistant."
    elif re.search(r'thank you|thanks', user_input):
        return "You're welcome!"
    elif re.search(r'bye|goodbye', user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that."

if __name__ == "__main__":
    print("Welcome to the Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r'bye|goodbye', user_input.lower()):
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
