class AIJobScorer:

    def __init__(self):
        pass

    def score(self, job):

        score = 0

        title = job.title.lower()
        company = job.company.lower()
        location = job.location.lower()
        salary = str(job.salary).lower()

        preferred = {
            "customer support": 45,
            "customer service": 45,
            "chat support": 45,
            "chat agent": 40,
            "call center": 40,
            "back office": 40,
            "data entry": 40,
            "content moderator": 45,
            "moderator": 35,
            "ai trainer": 50,
            "ai evaluator": 50,
            "virtual assistant": 40,
            "social media": 35,
            "support": 25,
        }

        for keyword, points in preferred.items():
            if keyword in title:
                score += points

        companies = {
            "concentrix": 20,
            "telus": 20,
            "foundever": 20,
            "teleperformance": 20,
            "majorel": 20,
            "welocalize": 20,
            "outlier": 15,
            "invisible": 15,
            "modsquad": 15,
            "keywords": 15,
        }

        for keyword, points in companies.items():
            if keyword in company:
                score += points

        if "remote" in location:
            score += 25
        elif "hybrid" in location:
            score += 15

        if "romanian" in title:
            score += 20

        digits = "".join(filter(str.isdigit, salary))

        if digits:
            value = int(digits)
            if value >= 3500:
                score += 20

        bad = {
            "developer": -50,
            "engineer": -45,
            "architect": -50,
            "manager": -25,
            "sales": -15,
            "java": -50,
            "python": -40,
            "devops": -50,
            "senior": -20,
        }

        for keyword, penalty in bad.items():
            if keyword in title:
                score += penalty

        score = max(0, min(score, 100))

        return score