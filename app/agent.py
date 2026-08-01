from app.filter import JobFilter
from app.scoring import JobScorer
from app.ai.job_scorer import AIJobScorer
from app.ai.job_validator import JobValidator
from app.ai.job_ranker import JobRanker
from app.ai.experience_filter import ExperienceFilter
from app.ai.country_language_filter import CountryLanguageFilter
from app.ai.job_classifier import JobClassifier
from app.ai.email_generator import EmailGenerator
from app.ai.smart_apply import SmartApply
from app.ai.job_stats import JobStats
from app.ai.profile_job_filter import ProfileJobFilter
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

        self.ai_scorer = AIJobScorer()
        self.validator = JobValidator()
        self.ranker = JobRanker()
        self.experience_filter = ExperienceFilter()
        self.country_filter = CountryLanguageFilter()
        self.classifier = JobClassifier()
        self.email_generator = EmailGenerator()
        self.smart_apply = SmartApply()
        self.stats = JobStats()
        self.profile_filter = ProfileJobFilter()

        self.telegram = TelegramBot()

        self.cv = CVManager()
        self.apply = ApplyManager()

    def send_digest(self, jobs):

        if not jobs:
            return

        summary = self.stats.generate_summary(jobs)
        top_jobs = self.ranker.top(jobs, 10)

        mesaj = "🤖 Job Hunter AI\n\n"
        mesaj += f"{summary}\n\n"
        mesaj += f"📋 Top {len(top_jobs)} joburi recomandate:\n\n"

        for index, job in enumerate(top_jobs, start=1):
            category = self.classifier.classify(job)

            mesaj += (
                f"{index}. 💼 {job.title}\n"
                f"🏢 {job.company}\n"
                f"📍 {job.location}\n"
                f"💰 {job.salary}\n"
                f"⭐ Scor AI: {job.score}/100 | {category}\n"
                f"🔗 {job.url}\n\n"
            )

        rezultat = self.telegram.send_message(mesaj)

        if rezultat:
            print("📨 Raport Telegram trimis.")
        else:
            print("❌ Eroare Telegram.")

    def run(self):

        jobs = self.searcher.search()

        new_jobs = []

        for job in jobs:

            if not self.validator.is_real_job(job):
                print(f"🚫 Job fals ignorat: {job.title}")
                continue

            if not self.experience_filter.is_allowed_level(job):
                continue

            if not self.country_filter.is_valid(job):
                continue

            # Filtrare strictă după interesele tale profesionale
            if not self.profile_filter.is_relevant(job):
                continue

            old_score = self.scorer.calculate(job)
            ai_score = self.ai_scorer.score(job)

            job.score = int((old_score + ai_score) / 2)

            print(f"🤖 {job.title} -> AI Score: {job.score}")

            if self.filter.is_valid(job):

                if self.manager.add_job(job):

                    if self.cv.exists() and self.smart_apply.should_apply(job):
                        custom_email = self.email_generator.generate(job)
                        print(f"✉️ Email generat pentru {job.company}:\n{custom_email[:100]}...\n")

                        self.apply.create_application(
                            job,
                            self.cv.get_path()
                        )

                    new_jobs.append(job)

        self.manager.save_jobs()

        new_jobs = self.ranker.rank(new_jobs)

        self.send_digest(new_jobs)

        return new_jobs