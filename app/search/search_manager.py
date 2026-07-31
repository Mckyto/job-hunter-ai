from app.search.romania_searcher import RomaniaSearcher
from app.search.remote_searcher import RemoteSearcher
from app.search.remotive_searcher import RemotiveSearcher
from app.search.remoteok_searcher import RemoteOKSearcher
from app.search.demo_searcher import DemoSearcher


class SearchManager:

    def __init__(self, config):

        self.config = config
        self.searchers = []

        sources = self.config.get("sources", {})

        if sources.get("romania", True):
            self.searchers.append(RomaniaSearcher())

        if sources.get("remote", True):
            self.searchers.append(RemoteSearcher())
            self.searchers.append(RemotiveSearcher())
            self.searchers.append(RemoteOKSearcher())

        if sources.get("demo", False):
            self.searchers.append(DemoSearcher())

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