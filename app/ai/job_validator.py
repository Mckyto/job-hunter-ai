class JobValidator:

    def __init__(self):

        self.blacklist = [

            "software engineer",
            "software developer",
            "developer",
            "full stack",
            "backend",
            "frontend",
            "ios",
            "android developer",
            "java",
            "python developer",
            "php",
            "react",
            "angular",
            "golang",
            "devops",
            "cloud",
            "architect",
            "tech lead",
            "engineering manager",
            "principal engineer",
            "staff engineer",
            "product engineer",
            "senior engineer",
            "machine learning engineer",
            "ai engineer",
            "data scientist",
            "scrum master",
            "qa automation",
            "site reliability",
            "sre"
        ]

        self.fake_titles = [

            "job title",
            "join our team",
            "future job",
            "future jobs",
            "current vacancies",
            "vacancy",
            "read more",
            "next steps",
            "other",
            "test",
            "mes",
            "political",
            "houseman",
            "flo",
            "reeder",
            "job opening",
            "opportunities",
            "apply here",
            "expression of interest",
            "spontaneous application",
            "career opportunities"
        ]

    def is_real_job(self, job):

        title = job.title.lower().strip()

        if len(title) < 5:
            return False

        for word in self.fake_titles:
            if word in title:
                return False

        for word in self.blacklist:
            if word in title:
                return False

        return True