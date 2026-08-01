class JobScorer:
    """
    Calculează scorul de bază pentru un job pe baza salariului și a criteriilor.
    """
    def __init__(self, config=None):
        self.config = config

    def calculate(self, job) -> int:
        salary_raw = getattr(job, 'salary', '0')
        
        # Extragem cifrele în siguranță, prevenind erorile dacă șirul este gol sau "Nespecificat"
        digits = "".join(filter(str.isdigit, str(salary_raw)))
        salary = int(digits) if digits else 0

        # Scor de bază orientativ
        base_score = 50
        
        if salary > 6000:
            base_score = 85
        elif salary > 4000:
            base_score = 70
        elif salary > 0:
            base_score = 60
        else:
            base_score = 50  # Valoare standard dacă salariul nu este specificat

        return base_score