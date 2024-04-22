## First Scraper

This is scraping project was made while referring to [Scrapy Course](https://www.youtube.com/watch?v=mBoX_JCKZTE) by Joe Kearney published in [FreeCodeCamp Youtube Channel](https://www.youtube.com/@freecodecamp).

### Stuff I Learned in this project.

- What frameworks and libraries to use for scraping project.
- Architecting a scraping project with scrapy.
- Learned to initiate project using `scrapy startproject bookscraper .` command.
- Made my first spider using `scrapy genspider bookspider books.toscrape.com`

### Running this project

#### Clone/Fork the project

`git clone git@github.com:naseemshah/scraping-labs.git`

#### Setup the virtual environment.

`cd first-scraper`

`python -m venv .venv`

#### Activate environment

`source .venv/bin/activate`

#### Running the book scraping spider

Open spiders folder

`cd bookscraper && cd spiders`

Run spider crawler, the output will be in books.csv

`scrapy crawl bookspider -o books.csv`
