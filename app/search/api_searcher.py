from app.search.demo_searcher import DemoSearcher


class SearchManager:

    def __init__(self):

        self.searchers = []

        # Searcher demo
        self.searchers.append(DemoSearcher())

        # Searchere reale (se vor activa ulterior)
        # self.searchers.append(JobicySearcher())
        # self.searchers.append(RemoteOKSearcher())
        # self.searchers.append(ArbeitnowSearcher())

    def search(self):

        all_jobs = []

        print("\n🔎 Încep căutarea pe toate sursele...\n")

        for searcher in self.searchers:

            try:

                print(f"➡️ {searcher.__class__.__name__}")

                jobs = searcher.search()

                print(f"   {len(jobs)} joburi găsite")

                all_jobs.extend(jobs)

            except Exception as e:

                print(f"❌ Eroare în {searcher.__class__.__name__}: {e}")

        print(f"\n✅ Total joburi găsite: {len(all_jobs)}\n")

        return all_jobs