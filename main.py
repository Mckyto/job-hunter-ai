from app.config import load_config
from app.job_manager import JobManager
from app.filter import JobFilter
from app.scoring import JobScorer
from app.search.demo_searcher import DemoSearcher
from app.logger import setup_logger


def main():

    logger = setup_logger()

    logger.info("Pornire Job Hunter AI")

    config = load_config()

    print("=" * 50)
    print("🤖 Job Hunter AI")
    print("=" * 50)

    manager = JobManager()
    job_filter = JobFilter(config)
    scorer = JobScorer(config)

    searcher = DemoSearcher()

    logger.info("Cautare joburi inceputa")

    print("\n🔎 Caut joburi...\n")

    found_jobs = searcher.search()

    logger.info(f"Gasite {len(found_jobs)} joburi")

    print(f"Au fost găsite {len(found_jobs)} joburi.")

    print("\n🧠 Analizez potrivirea...\n")

    accepted = 0
    rejected = 0
    duplicates = 0

    for job in found_jobs:

        job.score = scorer.calculate(job)

        print(f"{job.title} → Scor AI: {job.score}/100")

        if job_filter.is_valid(job):

            if manager.add_job(job):
                print("✅ Adăugat\n")
                accepted += 1
                logger.info(f"Job adaugat: {job.title}")

            else:
                duplicates += 1
                logger.info(f"Duplicat ignorat: {job.title}")

        else:
            print("❌ Respins\n")
            rejected += 1
            logger.info(f"Job respins: {job.title}")


    manager.list_jobs()

    manager.save_jobs()

    logger.info(
        f"Finalizare: acceptate={accepted}, respinse={rejected}, duplicate={duplicates}"
    )

    print("\n📊 Rezumat:")
    print(f"Acceptate: {accepted}")
    print(f"Respinse: {rejected}")
    print(f"Duplicate: {duplicates}")


if __name__ == "__main__":
    main()