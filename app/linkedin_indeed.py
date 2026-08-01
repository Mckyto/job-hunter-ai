import requests
from bs4 import BeautifulSoup

class JobItem:
    def __init__(self, title, company, location, salary, url):
        self.title = title
        self.company = company
        self.location = location
        self.salary = salary
        self.url = url
        self.score = 0

class LinkedInIndeedSearcher:
    """
    Caută joburi pe Indeed România și LinkedIn (poziții remote / România).
    """
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def search(self):
        all_jobs = []
        
        # 1. Indeed România
        try:
            url_indeed = "https://ro.indeed.com/jobs?q=operator+call+center+remote&l=Rom%C3%A2nia"
            response = requests.get(url_indeed, headers=self.headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                job_cards = soup.find_all('div', class_='cardOutline') or soup.find_all('div', class_='job_seen_beacon')
                for card in job_cards[:10]:
                    title_el = card.find('h2', class_='jobTitle') or card.find('a', class_='jcs-JobTitle')
                    title = title_el.text.strip() if title_el else "Poziție Indeed"
                    link_el = card.find('a', class_='jcs-JobTitle') or card.find('a')
                    link = link_el.get('href') if link_el and link_el.has_attr('href') else url_indeed
                    if not link.startswith('http'):
                        link = "https://ro.indeed.com" + link
                    all_jobs.append(JobItem(title, "Indeed Employer", "Romania / Remote", "Nespecificat", link))
            print(f"✅ Indeed Searcher: joburi procesate")
        except Exception as e:
            print(f"⚠️ Indeed Searcher eroare: {e}")

        # 2. LinkedIn Public Jobs (Romania / Remote)
        try:
            url_linkedin = "https://www.linkedin.com/jobs/search?keywords=Customer%20Support%20Remote%20Romania&location=Romania"
            response = requests.get(url_linkedin, headers=self.headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                job_cards = soup.find_all('div', class_='base-card') or soup.find_all('li')
                for card in job_cards[:10]:
                    title_el = card.find('h3', class_='base-search-card__title') or card.find('h4')
                    title = title_el.text.strip() if title_el else "Poziție LinkedIn"
                    link_el = card.find('a', class_='base-card__full-link') or card.find('a')
                    link = link_el.get('href') if link_el and link_el.has_attr('href') else url_linkedin
                    all_jobs.append(JobItem(title, "LinkedIn Employer", "Romania / Remote", "Nespecificat", link))
            print(f"✅ LinkedIn Searcher: joburi procesate")
        except Exception as e:
            print(f"⚠️ LinkedIn Searcher eroare: {e}")

        return all_jobs