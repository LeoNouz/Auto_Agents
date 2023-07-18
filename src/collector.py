# collector.py
import requests
from bs4 import BeautifulSoup

GOOGLE_SEARCH_API = "https://www.google.com/search?q="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

def get_user_query():
    """
    Function to get the user's query for the Google search.
    """
    user_query = input("Enter your query for Google search: ")
    return user_query

def perform_google_search(query):
    """
    Function to perform a Google search based on the user's query and return search results.
    """
    headers = {"User-Agent": USER_AGENT}
    params = {"q": query}

    response = requests.get(GOOGLE_SEARCH_API, headers=headers, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        search_results = []
        for result in soup.find_all("div", class_="tF2Cxc"):
            title = result.h3.text
            link = result.a["href"]
            snippet = result.find("div", class_="aCOpRe").div.text
            search_results.append({"title": title, "link": link, "snippet": snippet})
        return search_results
    else:
        raise Exception("Google search request failed.")

def save_search_results(results):
    """
    Function to save the Google search results to "query_search_result.txt" file.
    """
    with open("data/query_search_result.txt", "w", encoding="utf-8") as file:
        for result in results:
            file.write(f"Title: {result['title']}\n")
            file.write(f"Link: {result['link']}\n")
            file.write(f"Snippet: {result['snippet']}\n\n")

    print("Search results saved to 'query_search_result.txt'.")

if __name__ == "__main__":
    try:
        print("Collector: Gathering information from the user...")
        user_query = get_user_query()

        print(f"Collector: Performing Google search for '{user_query}'...")
        search_results = perform_google_search(user_query)

        print("Collector: Saving search results...")
        save_search_results(search_results)

        print("Collector: Information collection completed.")
    except Exception as e:
        print("Collector: An error occurred during information collection:", e)
