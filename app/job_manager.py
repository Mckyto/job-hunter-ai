import json
from pathlib import Path

from app.job import Job
from app.duplicate_checker import DuplicateChecker


class JobManager:

    def __init__(self):

        self.jobs = []
        self.file = Path("data/jobs.json")
        self.existing_jobs = self.load_jobs()


    def load_jobs(self):

        if not self.file.exists():
            return []

        with open(self.file, "r", encoding="utf-8") as file:
            return json.load(file)


    def add_job(self, job: Job):

        checker = DuplicateChecker(self.existing_jobs)

        if checker.is_duplicate(job):
            print(f"⚠️ Duplicat ignorat: {job.title}")
            return False


        self.jobs.append(job)


        self.existing_jobs.append({
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "salary": job.salary,
            "source": job.source,
            "url": job.url,
            "score": job.score
        })


        return True



    def save_jobs(self):

        self.file.parent.mkdir(exist_ok=True)


        with open(self.file, "w", encoding="utf-8") as file:

            json.dump(
                self.existing_jobs,
                file,
                ensure_ascii=False,
                indent=4
            )


        print("\n✅ Joburile noi au fost salvate.")



    def list_jobs(self):

        print(
            f"\nAu fost găsite {len(self.jobs)} joburi noi:\n"
        )


        for index, job in enumerate(self.jobs, start=1):

            print("=" * 50)
            print(f"Job #{index}")
            job.display()