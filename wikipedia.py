import requests

# Define the Wikipedia API URL for most popular articles
api_url = "https://en.wikipedia.org/w/api.php"

# Define the parameters for the API request
params = {
    "action": "query",
    "format": "json",
    "list": "mostviewed",
    "pvimlimit": "100",  # Number of results you want, change as needed
}

try:
    # Send an HTTP GET request to the Wikipedia API
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an exception for any HTTP errors

    data = response.json()

    # Extract the list of most-viewed articles
    most_viewed_articles = data["query"]["mostviewed"]

    # Create or open a text file for writing
    with open("most_viewed_articles.txt", "w", encoding="utf-8") as file:
        # Loop through and write the titles of the most-viewed articles to the file
        for i, article in enumerate(most_viewed_articles, start=1):
            title = article["title"]
            file.write(f"{i}. {title}\n")

    print("Most-viewed articles written to most_viewed_articles.txt.")
except requests.exceptions.RequestException as e:
    print("Error:", e)
except KeyError:
    print("Failed to retrieve most-viewed articles from Wikipedia API.")
