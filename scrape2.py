import requests
import bs4
from Chapter import Chapter
import time
from pathlib import Path
from dotenv import load_dotenv


def get_soup(url):
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    return soup


def get_links(soup):
    links = []
    div = soup.find(
        "div",
        class_="wp-block-group is-layout-grid wp-container-core-group-is-layout-7d05cc0d wp-block-group-is-layout-grid",
    )
    for href in div.find_all("a", class_="wp-block-latest-posts__post-title"):
        link = href.get("href")
        links.append(link)
    return links


def get_title(soup):
    div = soup.find(
        "div",
        class_="wp-block-group is-layout-constrained wp-block-group-is-layout-constrained",
    )
    try:
        title = div.find("h1")
    except AttributeError:
        print("Cannot find <h1> title, returning div")
        # print(div.text)
        return div

    print(f'"{title.text}"')
    return title


def get_paragraphs(soup):
    clean_paragraphs = []
    block = soup.find("div", class_="entry-content")
    paragraphs = block.find_all(["p", "hr", "ol", "blockquote", "pre", "ul"])
    for p in paragraphs:
        if p.name == "hr" and "wp-block-separator" in p.get("class", []):
            break
        else:
            del p["class"]
            clean_paragraphs.append(str(p))
    clean_paragraphs_string = "\n".join(clean_paragraphs)
    return clean_paragraphs_string


def main():
    load_dotenv()
    soup = get_soup(URL2)
    links = get_links(soup)
    chapter_objects = []
    for link in links:
        soup = get_soup(link)
        title = get_title(soup)
        print(title.text)
        if "side-story" in str(title):
            break
        body = get_paragraphs(soup)
        chapter_object = Chapter(title=title.text.strip(), content=body)
        chapter_objects.append(chapter_object)
        time.sleep(2)
    return chapter_objects


if __name__ == "__main__":
    main()
