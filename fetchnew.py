import requests

# Configuration
NEWS_API_KEY = "cee920762e97456ab99cea68f43d4d2a"
TOPIC = "artificial intelligence"
URL = f"https://newsapi.org/v2/everything?q={TOPIC}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"

# Fetch latest news
def fetch_news():
    response = requests.get(URL)
    data = response.json()
    
    if data.get("status") != "ok":
        print("Error fetching news:", data.get("message"))
        return []

    articles = data.get("articles", [])
    news_list = []

    for article in articles:
        title = article.get("title")
        description = article.get("description")
        content = article.get("content")
        url = article.get("url")
        
        news_item = f"Title: {title}\nDescription: {description}\nURL: {url}\n"
        news_list.append(news_item)

    return news_list

# Run and print
if __name__ == "__main__":
    news = fetch_news()
    for i, article in enumerate(news, 1):
        print(f"\nArticle {i}:\n{article}")
