# main.py
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.dirname(current_dir)
sys.path.append(project_root_dir)

from src.collector import get_user_query, perform_google_search, save_search_results
from src.chatgpt_integration import summarize_with_chatgpt, save_summary_to_file
from src.python_hub import run_python_hub

def main():
    try:
        # Step 1: Collect information from the user
        print("Step 1: Collecting information from the user...")
        user_query = get_user_query()
        search_results = perform_google_search(user_query)
        save_search_results(search_results)
        print("Step 1: Information collection completed.")

        # Step 2: Summarize information with ChatGPT
        print("Step 2: Summarizing information using ChatGPT...")
        summarized_info = summarize_with_chatgpt("\n".join(search_results))
        save_summary_to_file(summarized_info)
        print("Step 2: Information summarized using ChatGPT.")

        # Step 3: Run Python Hub for agent conversation and content generation
        run_python_hub()

        print("All steps completed successfully.")
    except Exception as e:
        print("An error occurred during the process:", e)

if __name__ == "__main__":
    main()
