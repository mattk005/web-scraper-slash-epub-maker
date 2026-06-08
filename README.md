# Matt's webscraper/EPUB maker

---

- A webscraper for collecting web fiction and generating an ePub for reading
  offline (ie. on a Kindle/Boox tablet etc.)
- retains the structure of the web page (Chapter order), can scrape either the
  novel index or start from chapter 1 and follow the "next chapter" buttons
  (scrape.py and scrape2.py)
- requirements.txt is included but this is mostly just beautiful soup 4,
  dotenv, requests and ebooklib.

---

This worked for the one book I wanted from the one site I was looking at.
I've since begun re-writing this project in golang for the next book I'm looking
at

---

Chapter data is found by finding the containing div, then typically using the `<hr>`
tag at the end of the chapter.
some example HTML:

```HMTL
<div class="entry-content wp-block-post-content is-layout-constrained wp-block-post-content-is-layout-constrained">

<p class="wp-block-paragraph">There was no reason to read the rest.</p>

<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide" />
```

Uses beautiful soup to find the top and bottom of the chapter text and collects
the `<p>` tags, retains nested tags (ePub format uses XHTML tags anyway), strips
the css tags.

```
    block = soup.find("div", class_="entry-content")
    paragraphs = block.find_all(["p", "hr", "ol", "blockquote", "pre", "ul"])
    for p in paragraphs:
        if p.name == "hr" and "wp-block-separator" in p.get("class", []):
            break
        else:
            del p["class"]
            clean_paragraphs.append(str(p))
```

Most of the other information such as URL and series Title/Author are hidden in
a .env. URL was the URL to chapter 1. URL2 was the URL to the series index. The
rest of the ePub creation was more manual than I would have liked.

```
def main():
    load_dotenv()
    TITLE = os.getenv("TITLE")
    AUTHOR = os.getenv("AUTHOR")
    ID = os.getenv("ID")
    COVER = os.getenv("COVER")
```

As mentioned above, scrape.py would find the next button to traverse the chapters.

```
    return soup.find("a", string=lambda t: t and "Next Chapter" in t).get("href")
```

scrape2.py just uses a div full of links to the chapters and preserves the order.

```
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
```
