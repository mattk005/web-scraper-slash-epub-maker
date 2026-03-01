from make_epub import make_book
from soup_to_chapter_list import get_chapter_objects, get_soup_list
from dotenv import load_dotenv
from ebooklib import epub
import os
import io


def main():
    load_dotenv()
    TITLE = os.getenv("TITLE")
    AUTHOR = os.getenv("AUTHOR")
    ID = os.getenv("ID")
    COVER = os.getenv("COVER")

    soup_list = get_soup_list()
    chapter_objects = get_chapter_objects(soup_list)
    book = make_book(
        chapter_objects=chapter_objects, TITLE=TITLE, AUTHOR=AUTHOR, ID=ID, COVER=COVER
    )
    epub.write_epub(f"./epub/{TITLE}.epub", book)
    f = io.BytesIO()
    epub.write_epub(f, book)
    f.seek(0)


if __name__ == "__main__":
    main()
