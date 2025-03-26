# Load data

# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 

# As a result, store all comments in chronological order in JSON and dump it to a file.

import json, time, requests

def fetch_news():

    url = "https://gnews.io/api/v4/top-headlines?country=ua&category=general&apikey=7b6a443b191af3cd0871b9a88fca132b"
    response = requests.get(url)

    try:
        data = json.loads(str(response.text ))
        response.raise_for_status()  # Raise exception for bad status codes
        news = []

        for item in data['articles']:
            news.append(item['title']+' - '+ item['url']+'\n')

        total_fetched = len(news)
        print(f"Fetched {total_fetched} news.")

    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

    return news

def save_to_file(news):
    filename = time.strftime('%d_%m_%Y')+'_'+'news'+'.txt'

    with open(filename, "w", encoding="utf-8") as file:
            json.dump(news, file, indent=4, ensure_ascii=False)


def main():

    # Fetch news
    print(f"Fetching news from link...")
    news = fetch_news()
    
    # Save to file
    if news:
        save_to_file(news)
    else:
        print("No news fetched.")

if __name__ == "__main__":
    main()
        
    