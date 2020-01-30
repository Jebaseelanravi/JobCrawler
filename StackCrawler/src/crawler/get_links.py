import requests
import lxml.html
import urllib.parse
from src.crawler.sharedqueues import input_queue


class Getlinks:

    def __init__(self):
        pass

    def get_links(self, link):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/54.0.2840.71 Safari/537.36'}
        resp = requests.get(link, headers=headers, timeout=10)
        content = resp.content
        tree = lxml.html.fromstring(content)
        links = tree.xpath("//a[@class='s-link stretched-link']/@href")
        for ol in links:
            # print(urllib.parse.urljoin("https://stackoverflow.com/", ol))
            input_queue.put(urllib.parse.urljoin("https://stackoverflow.com/", ol))

        next_page_link = tree.xpath("//span[text()='next']/ancestor::a/@href")
        if next_page_link:
            self.get_links(urllib.parse.urljoin("https://stackoverflow.com/", next_page_link[0]))
