# Leo30.py
import random
import time

def agent_leo30(input_message):
    # Customize Leo30's responses and behavior based on input_message
    response = "Leo30: This is a default response."

    # Implement the logic to handle different input messages and generate responses
    if "hello" in input_message.lower():
        response = "Leo30: Hi there! How can I be of service?"

    elif "how are you" in input_message.lower():
        response = "Leo30: I'm doing well, thank you!"

    elif "tell me a joke" in input_message.lower():
        jokes = [
            "Why don't some couples go to the gym? Because some relationships don't work out!",
            "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!",
            "Why don't skeletons fight each other? They don't have the guts!",
        ]
        response = f"Leo30: {random.choice(jokes)}"

    elif "thank you" in input_message.lower():
        response = "Leo30: You're welcome! If you need anything else, feel free to ask."

    else:
        response = "Leo30: I'm sorry, I didn't quite catch that. Could you repeat?"

    # Simulate some response time for the AI agent
    time.sleep(random.randint(1, 3))

    return response
