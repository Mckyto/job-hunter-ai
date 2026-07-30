from app.search.demo_searcher import DemoSearcher
from app.search.romania_searcher import RomaniaSearcher
from app.search.remote_searcher import RemoteSearcher


class SearchManager:

    def __init__(self):

        self.searchers = [

            RomaniaSearcher(),
            RemoteSearcher(),
            DemoSearcher()

        ]


    def search(self):

        jobs = []


        for searcher in self.searchers:

            try:

                results = searcher.search()

                jobs.extend(results)

                print(
                    f"✅ {searcher.__class__.__name__}: {len(results)} joburi găsite"
                )


            except Exception as e:

                print(
                    f"❌ Eroare la {searcher.__class__.__name__}: {e}"
                )


        return jobs