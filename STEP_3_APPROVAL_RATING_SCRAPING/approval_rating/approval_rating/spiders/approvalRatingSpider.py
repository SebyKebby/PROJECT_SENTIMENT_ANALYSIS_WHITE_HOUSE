import scrapy
from approval_rating.items import ApprovalItems

class ApprovalratingspiderSpider(scrapy.Spider):
    name = "approvalRatingSpider"
    allowed_domains = ["www.presidency.ucsb.edu"]
    start_urls = ["https://www.presidency.ucsb.edu/statistics/data/joseph-r-biden-public-approval"]

    def parse(self, response):
        table_rows = response.xpath("//div[@class='field-body']/table/tbody/tr")
        table_data = ApprovalItems()
        for table_row in table_rows:
            table_data['start_date'] = table_row.xpath("td[1]//text()").get() #Added // because the original code did not work since one element was nested in a "p" element (while others arent). 
            table_data['end_date']  = table_row.xpath("td[2]//text()").get()
            table_data['approving'] = table_row.xpath("td[3]//text()").get()
            table_data['disapproving'] = table_row.xpath("td[4]//text()").get()
            table_data['unsure'] = table_row.xpath("td[5]//text()").get()
            yield table_data
        
