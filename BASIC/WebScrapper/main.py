import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

all_jobs = []

for job in jobs:
    title = job.find("span", class_="title").text if job.find(
        "span", class_="title") else "Title not found"

    # company, position, region = job.find_all("span", class_="company")

    spans = job.find_all("span", class_="company")

    try:
        region = spans[2].text
    except:
        region = "Region not found"

    # tooltip--flag-logo 다음 것(a)을 찾아 href를 추출함
    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]

    '''
    url을 찾지 못하는 경우
    if url:
        url=url["href"]
    '''

    job_data = {
        "title": title,
        "company": spans[0].text,
        "position": spans[1].text,
        "region": region,
        "url": f"https://weworkremotely.com{url}"
    }

    all_jobs.append(job_data)


print(all_jobs)
