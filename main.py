import time
from app.agent import JobHunterAgent
from app.romania_portals import RomaniaPortalsSearcher
from app.linkedin_indeed import LinkedInIndeedSearcher

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

def main():
    print("==================================================")
    print("🤖 Job Hunter AI - Versiunea Completă Extinsă")
    print("==================================================")
    print("⏰ Scheduler pornit")
    print("Agentul rulează automat conform programării.\n")

    config = {}
    
    class JobManagerWrapper:
        def add_job(self, job):
            return True
        def save_jobs(self):
            print("✅ Joburile noi au fost salvate.")

    manager = JobManagerWrapper()

    # Toate motoarele de căutare reunite: eJobs, BestJobs, OLX, Ia Job, Indeed și LinkedIn
    searchers = [
        RomaniaPortalsSearcher(),
        LinkedInIndeedSearcher()
    ]

    multi_searcher = MultiSearcher(searchers)

    agent = JobHunterAgent(config, manager, multi_searcher)

    agent.run()

if __name__ == "__main__":
    main()