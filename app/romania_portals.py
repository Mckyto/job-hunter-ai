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

class RomaniaPortalsSearcher:
    """
    Caută joburi de pe platformele din România: eJobs, BestJobs, OLX și Ia Job,
    cu validare strictă a linkurilor.
    """
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Accept-Language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7"
        }

    def _is_valid_job_link(self, link, platform_domain):
        """Verifică dacă linkul este un job real și nu o pagină de categorie sau navigare."""
        if not link or platform_domain not in link:
            return False
        # Excludem cuvintele cheie care indică pagini generale/inactive
        invalid_keywords = ["/cautare", "/login", "/register", "/categorii", "/termeni", "/ajutor", "?page="]
        if any(kw in link for kw in invalid_keywords):
            return False
        return True

    def search(self):
        all_jobs = []
        
        # 1. Căutare eJobs
        try:
            url_ejobs = "https://www.ejobs.ro/locuri-de-munca/remote"
            response = requests.get(url_ejobs, headers=self.headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Căutăm elementele care conțin de obicei anunțurile
                job_cards = soup.find_all('div', class_='job-item') or soup.find_all('article')
                
                for card in job_cards[:10]:
                    title_el = card.find('h2') or card.find('h3') or card.find('a')
                    link_el = card.find('a', href=True)
                    
                    if link_el:
                        link = link_el['href']
                        if not link.startswith('http'):
                            link = "https://www.ejobs.ro" + link
                        
                        if self._is_valid_job_link(link, "ejobs.ro"):
                            title = title_el.text.strip() if title_el else "Poziție eJobs"
                            all_jobs.append(JobItem(title, "eJobs Employer", "Remote / România", "Nespecificat", link))
            print(f"✅ eJobs Searcher: joburi procesate")
        except Exception as e:
            print(f"⚠️ eJobs Searcher eroare: {e}")

        # 2. Căutare BestJobs
        try:
            url_bestjobs = "https://www.bestjobs.eu/ro/locuri-de-munca/remote"
            response = requests.get(url_bestjobs, headers=self.headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                job_cards = soup.find_all('article') or soup.find_all('div', class_='job-card')
                
                for card in job_cards[:10]:
                    title_el = card.find('h3') or card.find('h2')
                    link_el = card.find('a', href=True)
                    
                    if link_el:
                        link = link_el['href']
                        if not link.startswith('http'):
                            link = "https://www.bestjobs.eu" + link
                        
                        if self._is_valid_job_link(link, "bestjobs.eu"):
                            title = title_el.text.strip() if title_el else "Poziție BestJobs"
                            all_jobs.append(JobItem(title, "BestJobs Employer", "Romania / Remote", "Nespecificat", link))
            print(f"✅ BestJobs Searcher: joburi procesate")
        except Exception as e:
            print(f"⚠️ BestJobs Searcher eroare: {e}")

        # 3. Căutare OLX Locuri de muncă
        try:
            url_olx = "https://www.olx.ro/locuri-de-munca/"
            response = requests.get(url_olx, headers=self.headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                ads = soup.find_all('div', {'data-cy': 'l-card'}) or soup.find_all('tr', class_='wrap')
                
                for ad in ads[:10]:
                    title_el = ad.find('h4') or ad.find('h6')
                    link_el = ad.find('a', href=True)
                    
                    if link_el:
                        link = link_el['href']
                        if not link.startswith('http'):
                            link = "https://www.olx.ro" + link
                        
                        if self._is_valid_job_link(link, "olx.ro"):
                            title = title_el.text.strip() if title_el else "Poziție OLX"
                            all_jobs.append(JobItem(title, "OLX Employer", "Romania", "Nespecificat", link))
            print(f"✅ OLX Searcher: joburi procesate")
        except Exception as e:
            print(f"⚠️ OLX Searcher eroare: {e}")

        # 4. Căutare Ia Job (iajob.ro)
        try:
            url_iajob = "https://iajob.ro/"
            response = requests.get(url_iajob, headers=self.headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                job_listings = soup.find_all('div', class_='job-box') or soup.find_all('article')
                
                for job in job_listings[:10]:
                    title_el = job.find('h3') or job.find('h2')
                    link_el = job.find('a', href=True)
                    
                    if link_el:
                        link = link_el['href']
                        if not link.startswith('http'):
                            link = "https://iajob.ro" + link
                        
                        if self._is_valid_job_link(link, "iajob.ro"):
                            title = title_el.text.strip() if title_el else "Poziție IaJob"
                            all_jobs.append(JobItem(title, "IaJob Employer", "Romania", "Nespecificat", link))
            print(f"✅ IaJob Searcher: joburi procesate")
        except Exception as e:
            print(f"⚠️ IaJob Searcher eroare: {e}")

        return all_jobs
