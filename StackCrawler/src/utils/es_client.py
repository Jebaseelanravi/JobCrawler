from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()
import requests
import lxml.html
import json
import requests
import lxml.html
import json
url="https://stackoverflow.com/jobs/355830/python-django-developer-m-f-d-social-sweethearts-gmbh?so=i&pg=1&offset=-1&l=germany&u=Km&d=20"
resp = requests.get(url)

print(resp.status_code)
tree = lxml.html.fromstring(resp.content)
seo_data = tree.xpath("//script[@type='application/ld+json']/text()")
if seo_data:
    google_schema = json.loads(seo_data[0])
google_schema["url"]=url

res = es.index(index="stackcrawler", id=1, body=google_schema, doc_type="url")
print(res['result'])

res = es.get(index="stackcrawler", id=1, doc_type="url")
print(res['_source'])

es.indices.refresh(index="stackcrawler")

res = es.search(index="stackcrawler", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit)
    # print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
