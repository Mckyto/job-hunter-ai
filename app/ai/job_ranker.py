class JobRanker:
    """
    Sortează joburile în funcție de calitate.
    """

    def rank(self, jobs):

        if not jobs:
            return []

        return sorted(
            jobs,
            key=lambda job: (
                job.score,
                "remote" in str(job.location).lower(),
                "romanian" in str(job.title).lower(),
                len(str(job.title))
            ),
            reverse=True
        )

    def top(self, jobs, limit=10):
        return self.rank(jobs)[:limit]