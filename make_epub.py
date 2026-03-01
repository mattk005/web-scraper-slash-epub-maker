from ebooklib import epub
from dotenv import load_dotenv
import os
import io
from spaghetti import test_object


def make_book(chapter_objects, TITLE, AUTHOR, ID, COVER=None):
    book = epub.EpubBook()
    book.set_identifier(ID)
    book.set_title(TITLE)
    book.set_language("en")
    book.add_author(AUTHOR)
    # set cover image
    if COVER:
        img = epub.EpubImage()
        img.file_name = "cover.jpg"
        img.content = open(COVER, "rb").read()

        book.add_item(img)

        book.set_cover("cover.jpg", img.content)

    list_of_chapters = []
    for ch in chapter_objects:
        c = set_chapter(ch, book)
        list_of_chapters.append(c)

    # table of contents
    book.toc = list_of_chapters

    book.spine = list_of_chapters
    book.add_item(epub.EpubNav())  # Required for modern EPUB readers
    return book


def set_chapter(ch, book):
    c1 = epub.EpubHtml(
        title=ch.title,
        file_name=f"{ch.get_sanitized_title()}.xhtml",
        lang="en",
    )
    c1.set_content(f"<html><body><h1>{ch.title}</h1>{ch.paragraphs}</body></html>")
    book.add_item(c1)
    return c1


def main(chapter_objects):
    load_dotenv()
    TITLE = os.getenv("TITLE")
    AUTHOR = os.getenv("AUTHOR")
    ID = os.getenv("ID")
    book = make_book(chapter_objects=chapter_objects, TITLE=TITLE, AUTHOR=AUTHOR, ID=ID)
    return book


if __name__ == "__main__":
    test_chapter = test_object()
    book = main([test_chapter])
    epub.write_epub("./epub/test.epub", book)
    f = io.BytesIO()
    epub.write_epub(f, book)
    f.seek(0)
