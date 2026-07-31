from app.filter import JobFilter
from app.scoring import JobScorer
from app.notifications.telegram_bot import TelegramBot
from app.apply.apply_manager import ApplyManager
from app.apply.cv_manager import CVManager


class JobHunterAgent:

    def __init__(self, config, manager, searcher):

        self.config = config
        self.manager = manager
        self.searcher = searcher

        self.filter = JobFilter(config)
        self.scorer = JobScorer(config)

        self.telegram = TelegramBot()
        self.cv = CVManager()
        self.apply = ApplyManager()

    def send_digest(self, jobs):

        if not jobs:
            return

        jobs = sorted(
            jobs,
            key=lambda x: x.score,
            reverse=True
        )

        mesaj = "🔥 Job Hunter AI\n\n"
        mesaj += f"📌 {len(jobs)} joburi noi găsite\n\n"

        for index, job in enumerate(jobs[:10], start=1):

            mesaj += (
                f"{index}. 💼 {job.title}\n"
                f"🏢 {job.company}\n"
                f"📍 {job.location}\n"
                f"💰 {job.salary}\n"
                f"⭐ Scor: {job.score}\n"
                f"🔗 {job.url}\n\n"
            )

        rezultat = self.telegram.send_message(mesaj)

        if rezultat:
            print("📲 Raport Telegram trimis.")
        else:
            print("❌ Eroare trimitere Telegram.")

    def run(self):

        jobs = self.searcher.search()

        new_jobs = []

        for job in jobs:

            job.score = self.scorer.calculate(job)

            if self.filter.is_valid(job):

                if self.manager.add_job(job):

                    if self.cv.exists():
                        self.apply.create_application(
                            job,
                            self.cv.get_path()
                        )

                    new_jobs.append(job)

        self.manager.save_jobs()

        self.send_digest(new_jobs)

        return new_jobs