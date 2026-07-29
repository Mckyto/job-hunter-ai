class DuplicateChecker:

    def __init__(self, existing_jobs):
        self.existing_jobs = existing_jobs


    def is_duplicate(self, job):

        for existing in self.existing_jobs:

            if (
                existing["title"].lower() == job.title.lower()
                and
                existing["company"].lower() == job.company.lower()
            ):
                return True

        return False
