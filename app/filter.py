import unicodedata


class JobFilter:

    def __init__(self, config):
        self.config = config


    def normalize(self, text):

        text = unicodedata.normalize(
            "NFD",
            text
        )

        text = "".join(
            char for char in text
            if unicodedata.category(char) != "Mn"
        )

        return text.lower()


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

        job_location = self.normalize(job.location)

        for location in self.config["locations"]:

            if self.normalize(location) in job_location:
                return True

        return False


    def check_keyword(self, job):

        text = self.normalize(job.title)

        for keyword in self.config["keywords"]:

            if self.normalize(keyword) in text:
                return True

        return False


    def is_valid(self, job):

        return (
            self.check_salary(job)
            and self.check_location(job)
            and self.check_keyword(job)
        )