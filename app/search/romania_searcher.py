from app.search.base_searcher import BaseSearcher
from app.job import Job


class RomaniaSearcher(BaseSearcher):

    def search(self):

        return [

            Job(
                title="Customer Support Specialist",
                company="Romania Company",
                location="Bucuresti",
                salary="5000 lei",
                source="Romania Search",
                url="https://example.com/customer-support",
                score=0
            ),

            Job(
                title="Operator introducere date",
                company="Office Solutions",
                location="Bucuresti",
                salary="3800 lei",
                source="Romania Search",
                url="https://example.com/data-entry",
                score=0
            ),

            Job(
                title="Beauty Advisor Cosmetice",
                company="Beauty Store",
                location="Mega Mall Bucuresti",
                salary="3500 lei",
                source="Romania Search",
                url="https://example.com/beauty",
                score=0
            )

        ]