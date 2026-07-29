class JobScorer:

    def __init__(self, config):
        self.config = config


    def calculate(self, job):

        score = 0

        title = job.title.lower()
        location = job.location.lower()


        # Prioritate mare: joburi dorite
        high_priority = [
            "customer support",
            "customer service",
            "chat support",
            "chat agent",
            "data entry",
            "operator date",
            "back office"
        ]


        # Prioritate medie
        medium_priority = [
            "call center",
            "operator call center",
            "suport clienti",
            "consultant vanzari",
            "lucrator comercial"
        ]


        # Domenii bonus
        bonus_keywords = [
            "beauty",
            "cosmetice",
            "machiaj",
            "makeup",
            "mall",
            "magazin",
            "tutungerie"
        ]


        for keyword in high_priority:

            if keyword in title:
                score += 50
                break


        for keyword in medium_priority:

            if keyword in title:
                score += 35
                break


        for keyword in bonus_keywords:

            if keyword in title:
                score += 25
                break


        # Remote este un avantaj
        if "remote" in location:
            score += 20


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