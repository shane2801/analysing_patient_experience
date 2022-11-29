# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
import json

class MyscrapyprojectPipeline:

    # def open_spider(self, spider):
    #     self.file = open('items.json', 'w')
    #     self.file.write("[")

    # def close_spider(self,  spider):
    #     self.file.write("]")
    #     self.file.close()

    # def process_item(self, item, spider):
    #     line = json.dumps(ItemAdapter(item).asdict())+ "," + "\n"
    #     self.file.write(line)
    #     return item
    
    def open_spider(self, spider):
        self.filename_to_exporter = {}

    def close_spider(self, spider):
        for exporter, f in self.filename_to_exporter.values():
            exporter.finish_exporting()
            f.close()
        print("finished this one")

    def _exporter_for_item(self, item):
        filename = item.get('name')
        if filename not in self.filename_to_exporter:
            f = open(f'data/{filename}.json', 'wb')
            exporter = JsonItemExporter(f)
            exporter.start_exporting()
            self.filename_to_exporter[filename] = (exporter,f)
        return self.filename_to_exporter[filename][0]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item