import requests
import lxml.html
import json
from src.crawler.sharedqueues import output_queue,input_queue


def parse_job(self):
    while True:
        url=input_queue.get()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/54.0.2840.71 Safari/537.36'}
        resp = requests.get(url, headers=headers, timeout=10)
        content = resp.content
        tree = lxml.html.fromstring(content)
        seo_data = tree.xpath("//script[@type='application/ld+json']/text()")
        if seo_data:
            # print("Crawled :{}".format(url))
            google_schema = json.loads(seo_data[0])
            google_schema["url"]=url
            output_queue.put(google_schema)
