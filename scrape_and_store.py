import bs4
import re
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import time


def get_soup(url):
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    return soup


def get_title(soup):
    title = soup.find("h1", class_="wp-block-post-title")
    del title["class"]
    return title


def get_next_url(soup):
    # return soup.find("a", string="Next Chapter").get("href")
    return soup.find("a", string=lambda t: t and "Next Chapter" in t).get("href")


def sanitize_filename(filename):
    return re.sub(r"(?u)[^-\w.]", "-", filename)


def scrape_and_save(url, i):
    soup = get_soup(url)
    title_file_name = Path(
        (str(i).zfill(3) + sanitize_filename(get_title(soup).text + ".html"))
    ).name
    dir = Path(__file__).resolve()
    file_path = dir.parent / "chapters" / "html" / title_file_name
    with open(file_path, "w") as f:
        f.write(str(soup))
        print(f"Saved{title_file_name}")
    next_url = get_next_url(soup)
    return next_url


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("URL")
    my_set = set()

    i = 1
    while url not in my_set:
        my_set.add(url)
        url = scrape_and_save(url, i)
        i += 1
        time.sleep(2)
