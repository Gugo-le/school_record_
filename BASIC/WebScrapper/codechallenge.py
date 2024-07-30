import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    print(f"Scraping {url}...")
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }
    )
    soup = BeautifulSoup(response.content, "html.parser")


    jobs = soup.find_all("tr", class_="job")  

    print(f"Found {len(jobs)} jobs")

    for job in jobs:
        company = job.find("h3").text.strip() if job.find("h3") else "N/A"
        title = job.find("h2").text.strip() if job.find("h2") else "N/A"
        data = job.find_all("div", class_="location")
        region = data[0].text.strip() if len(data) > 0 and data[0] else "Not specified"
        salary = data[1].text.strip() if len(data) > 1 and data[1] else "Not specified"
        job_url = job.find("a")["href"] if job.find("a") else "N/A"
        job_data = {
            "company": company,
            "title": title,
            "region": region,
            "salary": salary,
            "url": f"https://remoteok.com/{job_url}"
        }
        all_jobs.append(job_data)

keywords = ["flutter", "python", "golang"]

for keyword in keywords:
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    scrape_page(url)

print("Number of jobs:", len(all_jobs))
for job in all_jobs:
    print(job)