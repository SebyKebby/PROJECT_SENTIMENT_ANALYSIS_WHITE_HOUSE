import scrapy


class WhitehousebriefingspiderSpider(scrapy.Spider):
    name = "whiteHouseBriefingSpider"
    allowed_domains = ["whitehouse.gov"]
    start_urls = ["https://www.whitehouse.gov/briefing-room/"]

    def parse(self, response):

        next_page = response.css('a.page-numbers ::attr(href)').get()
        for i in range(1,1078) :
            base_site = 'https://www.whitehouse.gov/briefing-room/page/'
            next_page = base_site + f'{i}/'
            i += 1
            yield response.follow(next_page, self.parse)
