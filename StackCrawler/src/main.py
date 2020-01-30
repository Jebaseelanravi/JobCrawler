from src.crawler.get_links import Getlinks
import threading
from src.crawler.parse_job_page import parse_job
from src.esclient.posting_indexer import PostingIndexer

if __name__ =="__main__":
    crawler=Getlinks()

    x = threading.Thread(target=crawler.get_links, args=("https://stackoverflow.com/jobs",))
    x.start()

    y=threading.Thread(target=parse_job,args=(1,))
    y.start()
    z=threading.Thread(target=PostingIndexer.index_document,args=(1,))
    z.start()



