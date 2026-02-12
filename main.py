import bs4
import requests
import os
from pathlib import Path
from dotenv import load_dotenv


def get_soup(url):
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    return soup


def for_testing():
    dir = Path(__file__).resolve()
    file = dir.parent / "chapters" / "Chapter 1.html"
    with open(file) as f:
        soup = bs4.BeautifulSoup(f, "html.parser")
    return soup


def get_title(soup):
    title = soup.find("h1", class_="wp-block-post-title")
    del title["class"]
    return title


def get_paragraphs(soup):
    clean_paragraphs = []
    block = soup.find("div", class_="entry-content")
    paragraphs = block.find_all(["p", "hr"])
    for p in paragraphs:
        if p.name == "hr" and "wp-block-separator" in p.get("class", []):
            break

        # elif p.text == "":
        #     continue
        else:
            del p["class"]
            clean_paragraphs.append(str(p))
    clean_paragraphs_string = "\n".join(clean_paragraphs)
    return clean_paragraphs_string


def get_next_url(soup):
    return soup.find("a", string="Next Chapter").get("href")


def write_out(title, body):
    dir = Path(__file__).resolve().parent / "chapters"
    dir.mkdir(parents=True, exist_ok=True)
    my_string = str(title) + "\n" + body
    with open(dir / title.text, "w") as f:
        f.write(my_string)


def scrape_and_save(url):
    soup = get_soup(url)
    # soup = for_testing()
    title = get_title(soup)
    body = get_paragraphs(soup)
    write_out(title, body)
    next_url = get_next_url(soup)
    return next_url


if __name__ == "__main__":
    load_dotenv()
    url = os.getenv("URL")
    scrape_and_save(url)
