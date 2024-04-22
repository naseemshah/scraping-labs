import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            nested_book_page_link = book.css("h3 a ::attr(href)").get()
            if 'catalogue/' in nested_book_page_link:
                book_url = 'https://books.toscrape.com/' + nested_book_page_link
            else:
                book_url = 'https://books.toscrape.com/catalogue/' + nested_book_page_link
            yield response.follow(book_url, callback = self.parse_book_page)

        next_page = response.css("li.next a ::attr(href)").get()

        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = 'https://books.toscrape.com/' + next_page
            else:
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            yield response.follow(next_page_url, callback = self.parse)

    def parse_book_page(self, response):
        pass