# python_hub.py
import sys
import os
from src.send_email import send_email
from utils.chatgpt_api import get_chatgpt_response
from agents.Leo13 import agent_leo13
from agents.Leo30 import agent_leo30

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.dirname(current_dir)
sys.path.append(project_root_dir)

def read_summary_info():
    """
    Function to read the summarized information from "summary_info_to_agents.txt" file.
    """
    with open(os.path.join("data", "summary_info_to_agents.txt"), "r", encoding="utf-8") as file:
        summary_info = file.read()
    return summary_info

def read_goal():
    """
    Function to read the user-defined goal from "goal.txt" file.
    """
    with open(os.path.join("data", "goal.txt"), "r", encoding="utf-8") as file:
        goal = file.read()
    return goal

def initialize_agents():
    """
    Function to initialize the AI agents, "Leo13.py" and "Leo30.py."
    Customize the agents' roles using the "system_role" parameter.
    """
    # Custom roles for Leo13 and Leo30. Modify as needed.
    leo13_role = "user"  # Change to "system" if Leo13 should play the system role.
    leo30_role = "system"  # Change to "user" if Leo30 should play the user role.

    # Initialize the Leo13 agent with the specified role.
    agent_leo13.initialize(system_role=leo13_role)

    # Initialize the Leo30 agent with the specified role.
    agent_leo30.initialize(system_role=leo30_role)

    print("Python Hub: AI agents Leo13 and Leo30 initialized with custom roles.")

def store_generated_content(content):
    """
    Function to store the generated content to "Youtube_idea.txt" and "AI_news.txt" files.
    """
    with open(os.path.join("data", "Youtube_idea.txt"), "w", encoding="utf-8") as file:
        file.write(content["youtube_idea"])

    with open(os.path.join("data", "AI_news.txt"), "w", encoding="utf-8") as file:
        file.write(content["ai_news"])

    print("Generated content saved successfully.")

def manage_agents_conversation(summary_info, goal):
    """
    Function to manage the conversation between the AI agents.

    Args:
        summary_info (str): The summarized information for the agents.
        goal (str): The user-defined goal for the conversation.

    Returns:
        dict: A dictionary containing the generated content for YouTube ideas and AI news.
    """
    # Define a dictionary to store the generated content for YouTube ideas and AI news
    generated_content = {
        "youtube_idea": "",
        "ai_news": "",
    }

    # Introduce the conversation
    conversation_intro = f"AI Agents Conversation:\nGoal: {goal}\nSummary: {summary_info}"
    print(conversation_intro)

    # Start the conversation between the agents
    leo13_message = f"Leo13: {goal}"
    leo30_message = ""

    for _ in range(3):  # Adjust the number of iterations as needed
        # Agent Leo13 responds to the current message
        leo13_response = agent_leo13(leo13_message)
        print(leo13_response)

        # Agent Leo30 processes Leo13's response using ChatGPT
        chatgpt_response = get_chatgpt_response(leo13_response)
        leo30_message = agent_leo30(chatgpt_response)

        # Agent Leo30 responds to the current message
        print(leo30_message)

        # Agent Leo13 processes Leo30's response using ChatGPT
        chatgpt_response = get_chatgpt_response(leo30_message)
        leo13_message = agent_leo13(chatgpt_response)

        # Store the generated content at each step for YouTube ideas and AI news
        generated_content["youtube_idea"] += f"{leo13_message}\n"
        generated_content["ai_news"] += f"{leo30_message}\n"

    return generated_content

def run_python_hub():
    try:
        print("Python Hub: Initiating agent conversation...")
        summary_info = read_summary_info()
        goal = read_goal()

        initialize_agents()

        # Call the function to manage the conversation between the agents.
        final_result = manage_agents_conversation(summary_info, goal)

        # Store the final result of the conversation
        store_generated_content(final_result)

        # Customize the email subject and recipient email address here.
        subject = "AI System Content"
        recipient_email = "recipient@example.com"

        # Send the email with the generated content.
        send_email.send_email(subject, recipient_email, final_result["youtube_idea"], final_result["ai_news"])

        print("Python Hub: Agent conversation completed. Content saved and email sent successfully.")
    except Exception as e:
        print("Python Hub: An error occurred during agent conversation or email sending:", e)

if __name__ == "__main__":
    run_python_hub()
