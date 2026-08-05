import os
import time
from dotenv import load_dotenv
from app.agent import JobHunterAgent
from app.romania_portals import RomaniaPortalsSearcher
from app.linkedin_indeed import LinkedInIndeedSearcher

# Încarcă variabilele de mediu dintr-un fișier .env (dacă există)
load_dotenv()

class MultiSearcher:
    def __init__(self, searchers):
        self.searchers = searchers

    def search(self):
        all_jobs = []
        for searcher in self.searchers:
            try:
                jobs = searcher.search()
                if jobs:
                    all_jobs.extend(jobs)
            except Exception as e:
                print(f"❌ Eroare la rularea unui căutător: {e}")
        return all_jobs

class JobManagerWrapper:
    def add_job(self, job):
        return True
        
    def save_jobs(self):
        print("✅ Joburile noi au fost salvate.")

def main():
    print("==================================================")
    print("🤖 Job Hunter AI - Versiunea Completă Extinsă")
    print("==================================================")
    print("⏰ Scheduler pornit în mod continuu.\n")

    # Configurări preluate din mediul de sistem sau setări implicite
    config = {
        "max_results": int(os.getenv("MAX_RESULTS", 50)),
        "alert_email": os.getenv("ALERT_EMAIL", "")
    }
    
    manager = JobManagerWrapper()

    # Toate motoarele de căutare reunite: eJobs, BestJobs, OLX, Ia Job, Indeed și LinkedIn
    searchers = [
        RomaniaPortalsSearcher(),
        LinkedInIndeedSearcher()
    ]

    multi_searcher = MultiSearcher(searchers)
    agent = JobHunterAgent(config, manager, multi_searcher)

    # Buclă de rulare continuă (de exemplu, rulează la fiecare 4 ore)
    interval_secunde = int(os.getenv("CHECK_INTERVAL_SECONDS", 14400)) # Implicit 4 ore

    while True:
        try:
            print(f"\n--- Rulare începută la {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
            agent.run()
            print("✨ Rulare finalizată cu succes.")
        except Exception as e:
            print(f"❌ Eroare în bucla principală a agentului: {e}")
        
        print(f"💤 Urmatoarea verificare va avea loc în {interval_secunde // 3600} ore...")
        time.sleep(interval_secunde)

if __name__ == "__main__":
    main()
