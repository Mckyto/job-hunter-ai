class JobFilter:
    """
    Filtrează joburile în funcție de diverse criterii (salariu, cuvinte cheie etc.).
    """
    def __init__(self, config=None):
        self.config = config

    def check_salary(self, job) -> bool:
        salary_raw = getattr(job, 'salary', '0')
        
        # Extragem cifrele în siguranță pentru a preveni erorile de tip ValueError
        digits = "".join(filter(str.isdigit, str(salary_raw)))
        salary = int(digits) if digits else 0
        
        # Verificăm dacă există o limită minimă de salariu setată în configurație
        min_salary = 0
        if isinstance(self.config, dict):
            min_salary = self.config.get('min_salary', 0)
        
        if min_salary and salary > 0 and salary < min_salary:
            return False
            
        return True

    def is_valid(self, job) -> bool:
        try:
            return self.check_salary(job)
        except Exception as e:
            print(f"⚠️ Eroare la filtrarea salariului: {e}")
            return True