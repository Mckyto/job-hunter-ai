from app.search.base_searcher import BaseSearcher
from app.job import Job


class RemoteSearcher(BaseSearcher):

    def search(self):

        return [

            Job(
                title="Romanian Chat Support Agent Remote",
                company="Remote Global",
                location="Remote",
                salary="6000 lei",
                source="Remote Search",
                url="https://example.com/chat-support",
                score=0
            ),

            Job(
                title="Romanian Data Entry Specialist Remote",
                company="Remote Data Company",
                location="Remote",
                salary="5000 lei",
                source="Remote Search",
                url="https://example.com/data-entry",
                score=0
            )

        ]