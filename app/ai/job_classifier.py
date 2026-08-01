class JobClassifier:
    """
    Clasifică joburile în categorii bazate pe scor: Perfect, Bun, Slab.
    """

    def classify(self, job) -> str:
        score = getattr(job, 'score', 0)
        
        if score >= 80:
            return "🌟 Perfect"
        elif score >= 50:
            return "👍 Bun"
        else:
            return "⚠️ Slab"