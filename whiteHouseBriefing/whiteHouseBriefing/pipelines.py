# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WhitehousebriefingPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        content = adapter.get('content')

        # REMOVE LATIN1 NON BREAKING (\xa0)
        if content:
            content = content.replace('\xa0', '')
            adapter['content'] = content
        return item
