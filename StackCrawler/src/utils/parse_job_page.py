import requests
import lxml.html
import json

resp = requests.get(
    "https://stackoverflow.com/jobs/355830/python-django-developer-m-f-d-social-sweethearts-gmbh?so=i&pg=1&offset=-1&l=germany&u=Km&d=20")
print(resp.status_code)
tree = lxml.html.fromstring(resp.content)
seo_data = tree.xpath("//script[@type='application/ld+json']/text()")
if seo_data:
    google_schema = json.loads(seo_data[0])

title = google_schema.get("title")
skils = google_schema.get("skills")
datePosted = google_schema.get("datePosted", None)
validThrough = google_schema.get("validThrough", None)
employmentType = google_schema.get("employmentType", None)
description = google_schema.get("description")
hiringOrganization = google_schema.get("hiringOrganization").get("name", None)
Country = google_schema.get("jobLocation")[0].get("address").get("addressCountry", None)
Locale = google_schema.get("jobLocation")[0].get("address").get("addressLocality", None)
experienceRequirements = google_schema.get("description", None)
VisaSponsor = 1 if "Visa sponsor" in description else 0

