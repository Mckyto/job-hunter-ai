import requests

from app.job import Job
from app.search.base_searcher import BaseSearcher


class RemoteOKSearcher(BaseSearcher):

    URL = "https://remoteok.com/api"

    def search(self):

        jobs = []

        try:

            response = requests.get(
                self.URL,
                headers={
                    "User-Agent": "JobHunterAI/1.0"
                },
                timeout=20
            )

            response.raise_for_status()

            data = response.json()

            # Primul element este metadata
            for item in data[1:]:

                jobs.append(

                    Job(
                        title=item.get("position", ""),
                        company=item.get("company", ""),
                        location=item.get("location", "Remote"),
                        salary="",
                        source="RemoteOK",
                        url="https://remoteok.com" + item.get("url", ""),
                        score=0
                    )

                )

        except Exception as e:

            print(f"❌ RemoteOKSearcher: {e}")

        return jobs