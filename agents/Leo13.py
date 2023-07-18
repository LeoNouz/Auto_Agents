# Leo13.py
import random
import time

def agent_leo13(input_message):
    # Customize Leo13's responses and behavior based on input_message
    response = "Leo13: This is a default response."

    # Implement the logic to handle different input messages and generate responses
    if "hello" in input_message.lower():
        response = "Leo13: Hello there! How can I assist you?"

    elif "how are you" in input_message.lower():
        response = "Leo13: I'm just an AI, so I don't have feelings, but thanks for asking!"

    elif "tell me a joke" in input_message.lower():
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
        ]
        response = f"Leo13: {random.choice(jokes)}"

    elif "thank you" in input_message.lower():
        response = "Leo13: You're welcome!"

    else:
        response = "Leo13: I'm sorry, I didn't understand that. Can you please rephrase?"

    # Simulate some response time for the AI agent
    time.sleep(random.randint(1, 3))

    return response
