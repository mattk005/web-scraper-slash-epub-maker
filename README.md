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
