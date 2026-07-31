class DuplicateChecker:

    def __init__(self, existing_jobs):

        self.existing_jobs = existing_jobs



    def find_existing(self, job):

        for existing in self.existing_jobs:

            if (
                existing["title"].lower() == job.title.lower()
                and
                existing["company"].lower() == job.company.lower()
            ):

                return existing


        return None



    def is_duplicate(self, job):

        existing = self.find_existing(job)

        if existing:

            return True


        return False



    def has_changes(self, job):

        existing = self.find_existing(job)


        if not existing:

            return False



        if existing.get("salary") != job.salary:
            return True


        if existing.get("url") != job.url:
            return True


        if existing.get("score") != job.score:
            return True


        return False