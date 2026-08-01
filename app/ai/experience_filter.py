class ExperienceFilter:
    """
    Filtrează joburile în funcție de nivelul de experiență.
    Elimină automat pozițiile de tip Senior, Lead, Manager, Director etc.
    """

    def is_allowed_level(self, job) -> bool:
        title = str(job.title).lower()
        
        # Cuvinte cheie care indică un nivel prea ridicat de experiență
        forbidden_keywords = [
            "senior", "lead", "manager", "director", 
            "head of", "principal", "staff", "architect", "vp"
        ]

        # Verificăm dacă titlul conține vreun termen interzis
        for keyword in forbidden_keywords:
            if keyword in title:
                print(f"🚫 Job respuns (nivel prea ridicat - '{keyword}'): {job.title}")
                return False

        return True