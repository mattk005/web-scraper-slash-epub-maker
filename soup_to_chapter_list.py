from make_epub import make_book
from Chapter import Chapter
from scrape_and_save import get_title, get_paragraphs
from pathlib import Path
import bs4


def get_soup_list():
    dir = Path(Path(__file__).parent / "chapters" / "html").resolve()
    list_of_soup = []
    for file_path in dir.iterdir():
        if str(file_path).endswith("html"):
            with open(file_path) as f:
                soup = bs4.BeautifulSoup(f, "html.parser")
                list_of_soup.append(soup)

    return list_of_soup


def get_chapter_objects(list_of_soup):
    chapter_objects = []
    for soup in list_of_soup:
        title = get_title(soup)
        paragraphs = get_paragraphs(soup)
        chapter_objects.append(Chapter(title=title, paragraphs=paragraphs))
    return chapter_objects
