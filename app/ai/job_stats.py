class JobStats:
    """
    Generează statistici și rapoarte despre joburile procesate.
    """

    def generate_summary(self, jobs) -> str:
        total = len(jobs)
        if total == 0:
            return "📊 Statistici: Nu există joburi procesate în această sesiune."

        perfect = sum(1 for j in jobs if getattr(j, 'score', 0) >= 80)
        good = sum(1 for j in jobs if 50 <= getattr(j, 'score', 0) < 80)
        weak = sum(1 for j in jobs if getattr(j, 'score', 0) < 50)

        summary = (
            f"📊 **Statistici Sesiune Job Hunter AI**\n"
            f"• Total joburi analizate: {total}\n"
            f"• 🌟 Perfect (>=80): {perfect}\n"
            f"• 👍 Bun (50-79): {good}\n"
            f"• ⚠️ Slab (<50): {weak}"
        )
        return summary