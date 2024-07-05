# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ApprovalRatingPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ##CLEANING ALL DATAS
        keys = ['start_date', 'end_date' , 'approving' , 'disapproving', 'unsure']
        for key in keys:
            key_value = adapter.get(key)
            key_value = key_value.strip()

        ## CLEANING THE DATE DATA
        date_keys = ['start_date', 'end_date']
        for date_key in date_keys:
            date_value = adapter.get(date_key)
            date_value = date_value.replace('-','/')
        return item


