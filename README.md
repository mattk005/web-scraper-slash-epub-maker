# Matt's webscraper/EPUB maker

---

The plan for this project is to scrape a certain webpage for a web novel I'm
interested in reading, then convert it's contents to some format my kindle
paperwhite will like. I already had a webscraper that Gemini put together in
like 10 seconds but we're doing this form scratch for a learning experience
(though the webscraper part isn't that complicated, it does have to be tailored
for the content we're scraping)

Luckily the page I'm scraping is formatted with each page being a chapter and
each paragraph properly wrapped in:

```HMTL
<p class="wp-block-paragraph">There was no reason to read the rest.</p>
```

From what I've seen EPUB files are just a zip folder with a pile of .xhtml files
in them, so hopefully I can just grab a template fill it up and call it a day.
