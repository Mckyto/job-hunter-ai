from datetime import datetime

from app.search.base_searcher import BaseSearcher
from app.job import Job


class DemoSearcher(BaseSearcher):

    def search(self):

        timestamp = datetime.now().strftime("%H:%M:%S")

        return [

            Job(
                title=f"Customer Support Specialist {timestamp}",
                company="Demo Company",
                location="București",
                salary="4800 lei",
                source="Demo Search",
                url=f"https://example.com/customer-support/{timestamp}",
                score=90
            ),

            Job(
                title="Data Entry Operator",
                company="Remote Company",
                location="Remote",
                salary="4100 lei",
                source="Demo Search",
                url="https://example.com/data-entry",
                score=85
            )

        ]