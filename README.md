# AI Content Generation System
The AI Content Generation System is a Python-based application that allows users to collect information from the web, summarize it using ChatGPT, and generate AI-generated content for YouTube ideas and AI news. The system comprises several modules, including data collection, AI agent interactions, summarization, and email communication.

## Features
- Collects user queries and performs a Google search to gather relevant information.
- Uses OpenAI's ChatGPT API for text summarization and restructuring.
- Employs AI agents "Leo13" and "Leo30" for conversation and content generation.
- Provides content for YouTube ideas and AI news.
- Sends generated content via email to a specified recipient.

## Prerequisites
Before running the system, ensure you have the following prerequisites:

- 1. Python 3.10 installed on your system.
- 2. Access to OpenAI's ChatGPT API and an API key.
- 3. OpenAI Python package installed (version used during development: openai==0.27.0).
- 4. An active internet connection to perform Google searches and interact with the ChatGPT API.

## Installation
- 1. Clone this repository to your local machine:
  ```
  git clone https://github.com/your-username/ai-content-generation.git
  ```
- 2. Change into the project directory:
  ```
  cd ai-content-generation
  ```
- 3. Install the required Python dependencies:
  ```
  pip install -r requirements.txt
  ```

## Configuration
To configure the system for your use, follow these steps:

- 1. Open the chatgpt_integration.py file and replace YOUR_OPENAI_API_KEY with your actual ChatGPT API key.
- 2. In the python_hub.py file, configure the AI agents' roles by changing leo13_role and leo30_role variables to either "user" or "system".
- 3. Set up your email server details in the send_email.py file by updating the smtp_server, smtp_port, smtp_username, and smtp_password variables.
- 4. Customize the email subject and recipient email address in the run_python_hub() function in the python_hub.py file.

## Usage
To use the AI Content Generation System:

- 1. Run the main.py script:
  ```
  python main.py
  ```
- 2. Follow the prompts to provide your query for the Google search.
- 3. The system will summarize the search results using ChatGPT.
- 4. AI agents "Leo13" and "Leo30" will engage in a conversation to generate content for YouTube ideas and AI news.
- 5. The generated content will be saved in data/Youtube_idea.txt and data/AI_news.txt.
- 6. The system will send the generated content via email to the specified recipient.

## Contributions
Contributions to the AI Content Generation System are welcome! Here's how you can contribute:

- 1. Fork the repository on GitHub.
- 2. Create a new branch from the main branch with a descriptive name for your feature or fix.
- 3. Implement your changes, ensuring to follow the existing code style and conventions.
- 4. Write unit tests for your code to maintain code quality.
- 5. Open a pull request against the main branch, describing your changes and improvements.
- 6. Your pull request will be reviewed by the maintainers, and upon approval, it will be merged into the main branch.

## License
The AI Content Generation System is open-source software licensed under the MIT License.

## Acknowledgments
Special thanks to OpenAI for providing access to the ChatGPT API and the community for valuable contributions and feedback.

Feel free to reach out to the maintainers with any questions or feedback. We hope you find the AI Content Generation System useful and enjoy contributing to its development!