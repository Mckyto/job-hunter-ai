from app.config import load_config
from app.job_manager import JobManager
from app.search.demo_searcher import DemoSearcher
from app.agent import JobHunterAgent
from app.logger import setup_logger


def main():

    logger = setup_logger()

    logger.info("Pornire Job Hunter AI")

    config = load_config()

    manager = JobManager()
    searcher = DemoSearcher()

    agent = JobHunterAgent(
        config=config,
        manager=manager,
        searcher=searcher
    )

    print("=" * 50)
    print("🤖 Job Hunter AI")
    print("=" * 50)

    print("\n🔎 Agentul caută joburi...\n")

    added = agent.run()

    print(f"\n✅ Joburi noi adăugate: {added}")

    logger.info(
        f"Agent finalizat. Joburi noi: {added}"
    )


if __name__ == "__main__":
    main()