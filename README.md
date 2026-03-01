# Matt's webscraper/EPUB maker

---

The plan for this project is to scrape a certain webpage for a web novel I'm
interested in reading, then convert it's contents to some format my kindle
paperwhite will like (an EPUB). I already had a webscraper that Gemini put
together in like 10 seconds but we're doing this form scratch for a learning
experience (the webscraper part isn't that complicated, it does have to be
tailored for the content we're scraping)

The scraper is being built for a
WordPress site so the body mostly looks like this:

```HMTL
<div class="entry-content wp-block-post-content is-layout-constrained wp-block-post-content-is-layout-constrained">

<p class="wp-block-paragraph">There was no reason to read the rest.</p>

<hr class="wp-block-separator has-alpha-channel-opacity is-style-wide" />
```

^^ the gist of it is that we're using the div to have the start of the content
we're interested in and then the horizontal rule as a mark to the end of the
content, then `return soup.find("a", string="Next Chapter").get("href")` will
give us the URL for the next chapter.

From what I've seen EPUB files are just a zip folder with a pile of .xhtml files
in them, so hopefully I can just grab a template fill it up and call it a day.

## Update 1

webscraper is working and looks pretty. Currently it writes the title and body
to a file in chapters/ next is the hard part: finding a decent template for an
EPUB. I'll deal with looping scraper once I have an XHTML template for the chapters.

## Update 2

I ended up scraping and storing all of the chapters in chapters/html/ (ignored
in .gitignore) I've decided I'm going to be using EbookLib. I'll eventually make
the scraper look nice but for now I want to see if I can get this into a format
that e-readers like.

The pivot to EbookLib is a little disappointing but I'm pretty sure that EPUBs
are going to be far more strict and pedantic than I had originally expected.

## Update 3

Everything seems to be working, I just need to refactor it all because it's
ugly. My actual workflow was to scrape all the pages I wanted. Then convert it
from my saved .html files in my folder. I'm not sure if I want the final project
to look like that. Originally I wanted it to do everything in memory, but I
didn't want to blast the website with requests every time I made a change.
