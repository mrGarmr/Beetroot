# Robots.txt
# Download and save to file robots.txt from wikipedia, twitter websites etc.

import requests, os.path

# List of websites
websites = [
    "https://www.wikipedia.org/robots.txt",
    "https://twitter.com/robots.txt",
    "https://www.google.com/robots.txt",
]

def download_robot():
    # Download and save each robots.txt file
    for url in websites:
        try:
            response = requests.get(url, timeout=5)  # Fetch the robots.txt file
            response.raise_for_status()  # Raise an error for bad status codes
            save_robot(url, response)

        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")

def save_robot(url, response):
    # Extract domain name for file naming
    domain = url.split("//")[1].split("/")[0]
    filename = f"{domain}_robots.txt"

    # Save the file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(response.text)

    print(f"Saved {filename}")

def main():
    download_robot()

if __name__ == "__main__":
    main()
        