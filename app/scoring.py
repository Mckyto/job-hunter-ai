class JobScorer:

    def __init__(self, config):
        self.config = config


    def calculate(self, job):

        score = 0

        title = job.title.lower()

        # Domeniu potrivit
        for keyword in self.config["keywords"]:
            if keyword.lower() in title:
                score += 40
                break


        # Locație potrivită
        for location in self.config["locations"]:
            if location.lower() in job.location.lower():
                score += 30
                break


        # Salariu
        if job.salary:
            salary = int(
                "".join(
                    filter(str.isdigit, job.salary)
                )
            )

            if salary >= self.config["salary_min"]:
                score += 30


        return min(score, 100)