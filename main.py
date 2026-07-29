from app.config import load_config
from app.job_manager import JobManager
from app.filter import JobFilter
from app.scoring import JobScorer
from app.search.demo_searcher import DemoSearcher


def main():

    config = load_config()

    print("=" * 50)
    print("🤖 Job Hunter AI")
    print("=" * 50)

    manager = JobManager()
    job_filter = JobFilter(config)
    scorer = JobScorer(config)

    searcher = DemoSearcher()

    print("\n🔎 Caut joburi...\n")

    found_jobs = searcher.search()

    print(f"Au fost găsite {len(found_jobs)} joburi.")

    print("\n🧠 Analizez potrivirea...\n")

    for job in found_jobs:

        job.score = scorer.calculate(job)

        print(f"{job.title} → Scor AI: {job.score}/100")

        if job_filter.is_valid(job):

            if manager.add_job(job):
                print("✅ Adăugat\n")

        else:
            print("❌ Respins de filtre\n")


    manager.list_jobs()

    manager.save_jobs()


if __name__ == "__main__":
    main()