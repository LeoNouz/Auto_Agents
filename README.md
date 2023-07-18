# AI-Autonomous-Agents

## Overview:
This repository contains an advanced AI System, an intelligent application designed to collect, summarize, and facilitate discussions between AI agents. The AI agents interact using the GPT-3.5 Chat API, and the system generates summary documents based on their conversations.

## Table of Contents:
- 1. Introduction
- 2. System Components
    + 2.1 Data Collection and Summary Generation
    + 2.2 AI Agents' Conversation
    + 2.3 Generating Summary Documents
    + 2.4 Sending Emails
- 3. Prerequisites
- 4. Setup and Configuration
    + 4.1 Installing Dependencies
    + 4.2 API Key Configuration
    + 4.3 Email Configuration
- 5. Usage Instructions
- 6. Contribution Guidelines
- 7. Conclusion

## 1. Introduction:
The AI System is an advanced solution designed to explore and discuss artificial intelligence news, generate a summary of the collected information, facilitate conversations between AI agents, generate summary documents for YouTube ideas and AI news, and finally, send these documents to a specified email address.

## 2. System Components:
The AI System consists of four main components:

### 2.1 Data Collection and Summary Generation (collector/collector.py):
- This component collects information from Google search results related to "artificial intelligence news."
- It extracts the titles and contents of the search results and generates a summary using the OpenAI GPT-3.5 Turbo API.
- The summary is saved to the "summary_info_to_agents.txt" file.

### 2.2 AI Agents' Conversation (python_hub.py):
- This component manages the conversation between two AI agents, named Leo13 and Leo30.
- Leo13 plays the role of the user, while Leo30 plays the role of the system.
- The AI agents take turns responding to each other using the GPT-3.5 Turbo API.
- The conversation continues for a predefined number of iterations.

### 2.3 Generating Summary Documents (python_hub.py):
- This component generates two summary documents:
  + "Youtube_idea.txt": Describing the winning idea for a YouTube video.
  + "AI_news.txt": Summarizing the top AI news stories discussed by the AI agents.
- The content in these documents is generated during the conversation between AI agents.

### 2.4 Sending Emails (send_email.py):
- This component reads the content of the "Youtube_idea.txt" and "AI_news.txt" files.
- It creates an email with the summary content and sends it to a specified recipient's email address.
- The email configuration should be set up correctly with valid email credentials.

## 3. Prerequisites:
- Python 3.10 or later installed on the system.
- An OpenAI GPT-3.5 Turbo API key.
- An email account for sending emails.

## 4. Setup and Configuration:

### 4.1 Installing Dependencies:
- Install the required Python packages using `pip`:
  ```
  pip install openai
  ```

### 4.2 API Key Configuration:
- Replace the placeholder API key in `src/chatgpt_integration.py` with your actual GPT-3.5 Turbo API key.

### 4.3 Email Configuration:
- Replace the email configurations (sender_email, recipient_email, smtp_server, smtp_port, smtp_username, smtp_password) in `src/send_email.py` with your actual email credentials.
- Make sure to allow less secure apps if using Gmail or follow the specific email provider's security guidelines.

## 5. Usage Instructions:
- Run the AI System using the following command in the terminal or command prompt:
  ```
  python python_hub.py
  ```
- The system will execute the four steps: Data Collection and Summary Generation, AI Agents' Conversation, Generating Summary Documents, and Sending Emails.

## 6. Contribution Guidelines:
We welcome contributions from the GitHub community. If you want to contribute to the AI System, follow these steps:
1. Fork the repository and create a new branch for your feature or bug fix.
2. Make the necessary changes and improvements.
3. Test your changes thoroughly.
4. Create a pull request to merge your changes into the main branch.
5. Our team will review your pull request, provide feedback, and merge it if it meets the project's guidelines.

## 7. Conclusion:
The AI System serves as an advanced example of how to integrate web scraping, AI agents, and the OpenAI GPT-3.5 Turbo API to automate data collection, facilitate meaningful conversations, and generate summary documents. By following the provided documentation and guidelines, you can adapt the system to different use cases and implement advanced algorithms for content generation. Remember to handle sensitive information securely and test the system thoroughly before deployment. Your contributions are valuable and will enhance the functionality and usability of the AI System.