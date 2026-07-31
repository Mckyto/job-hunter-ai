import requests

from app.job import Job
from app.search.base_searcher import BaseSearcher


class RemotiveSearcher(BaseSearcher):

    URL = "https://remotive.com/api/remote-jobs"

    def search(self):

        jobs = []

        try:

            response = requests.get(
                self.URL,
                timeout=20
            )

            response.raise_for_status()

            data = response.json()

            for item in data.get("jobs", []):

                jobs.append(

                    Job(
                        title=item.get("title", ""),
                        company=item.get("company_name", ""),
                        location=item.get("candidate_required_location", "Remote"),
                        salary=item.get("salary", ""),
                        source="Remotive",
                        url=item.get("url", ""),
                        score=0
                    )

                )

        except Exception as e:

            print(f"❌ RemotiveSearcher: {e}")

        print("\n===== PRIMELE JOBURI REMOTIVE =====")

        for job in jobs[:10]:
            print(job.title)

        print("===============================\n")

        return jobs