from elasticsearch import Elasticsearch
from src import settings
from src.crawler.sharedqueues import output_queue

es = Elasticsearch()


class PostingIndexer:

    def __init__(self):

        pass

    def index_document(self):
        while True:
            data = output_queue.get()
            res = es.index(index=settings.index, id=data.get("url"), body=data, doc_type="url")
            print("crawled :{}".format(data.get("url")))
