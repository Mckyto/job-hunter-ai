class SmartApply:
    """
    Decide inteligent dacă se face aplicarea automată în funcție de scorul jobului.
    """

    def should_apply(self, job) -> bool:
        score = getattr(job, 'score', 0)
        
        # Aplicăm automat doar dacă scorul este de cel puțin 50 (categoriile Bun sau Perfect)
        if score >= 50:
            print(f"✅ Smart Apply: Aprobat pentru '{job.title}' (Scor: {score})")
            return True
        else:
            print(f"⏳ Smart Apply: Oprit pentru '{job.title}' (Scor prea mic: {score})")
            return False