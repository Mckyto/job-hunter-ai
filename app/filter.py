from app.job import Job


class JobFilter:

    def __init__(self, config):
        self.config = config

    def check_salary(self, job):
        if not job.salary:
            return False

        salary = int(
            "".join(
                filter(str.isdigit, job.salary)
            )
        )

        return salary >= self.config["salary_min"]

    def check_location(self, job):
        for location in self.config["locations"]:
            if location.lower() in job.location.lower():
                return True

        return False

    def check_keyword(self, job):
        text = job.title.lower()

        for keyword in self.config["keywords"]:
            if keyword.lower() in text:
                return True

        return False

    def is_valid(self, job):
        return (
            self.check_salary(job)
            and self.check_location(job)
            and self.check_keyword(job)
        )