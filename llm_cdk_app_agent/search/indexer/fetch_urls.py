from urls import URLS
import requests
import os


def fetch_urls(URLS):
    if not os.path.exists(".cache"):
        os.makedirs(".cache")

    for url in URLS:
        print(url)
        # Get our output
        output = requests.get(url).text

        # Split the url name
        url_name = url.split(".")
        url_name = f"{url_name[-3]}_{url_name[-2]}"
        with open(f".cache/{url_name}.html", "w") as f:
            f.write(output)


def load_html():
    """Load html from cache."""
    docs = []
    for file in os.listdir(".cache"):
        with open(f".cache/{file}", "r") as f:
            docs.append(f.read())
    return docs


def split_docs(docs):
    """Split docs into sections."""
    pass


if __name__ == "__main__":
    # fetch_urls(URLS)

    # Load html from cache
    docs = load_html()
    print(docs)
