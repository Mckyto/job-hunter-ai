from app.search.demo_searcher import DemoSearcher


class SearchManager:

    def __init__(self):
        self.searchers = [
            DemoSearcher()
        ]

    def search(self):

        jobs = []

        for searcher in self.searchers:
            try:
                jobs.extend(searcher.search())
            except Exception as e:
                print(f"Eroare la {searcher.__class__.__name__}: {e}")

        return jobs