from app.filter import JobFilter
from app.scoring import JobScorer


class JobHunterAgent:

    def __init__(self, config, manager, searcher):
        self.config = config
        self.manager = manager
        self.searcher = searcher

        self.filter = JobFilter(config)
        self.scorer = JobScorer(config)


    def run(self):

        jobs = self.searcher.search()

        accepted = 0

        for job in jobs:

            job.score = self.scorer.calculate(job)

            if self.filter.is_valid(job):

                if self.manager.add_job(job):
                    accepted += 1

        self.manager.save_jobs()

        return accepted
