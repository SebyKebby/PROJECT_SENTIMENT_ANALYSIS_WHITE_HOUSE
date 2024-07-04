import scrapy

from whiteHouseBriefing.items import BriefingItem

class WhitehousebriefingspiderSpider(scrapy.Spider):
    name = "whiteHouseBriefingSpider"
    allowed_domains = ["whitehouse.gov"]
    start_urls = ["https://www.whitehouse.gov/briefing-room/"]

    def parse(self, response):

        briefings = response.css('a.news-item__title ::attr(href)')
        for briefing in briefings:
            next_url = briefing.get()
            yield response.follow(next_url, callback= self.parse_briefing)

        next_page = response.css('a.page-numbers ::attr(href)').get()
        for i in range(1,1080) :
            base_site = 'https://www.whitehouse.gov/briefing-room/page/'
            next_page = base_site + f'{i}/'
            yield response.follow(next_page, self.parse)
    def parse_briefing(self,response):
        briefing_item =BriefingItem()

        briefing_item['url']= response.url
        briefing_item['title']= ''.join(response.css('h1 ::text, h1 *::text').getall()).strip()
        briefing_item['briefing_type']= response.xpath("//ol[@class='wh-breadcrumbs__wrap']/li[3]/a/text()").get().strip()

        if briefing_item['briefing_type']:
            briefing_item['briefing_type'] = briefing_item['briefing_type'].strip()
        else:
            self.logger.warning(f"Briefing type not found on page: {response.url}")
            briefing_item['briefing_type'] = None

        briefing_item['date']= response.css('time ::text').get()
        briefing_item['content']= [item.strip() for item in response.css('div.row p ::text').getall()  if item.strip()]

        yield briefing_item

