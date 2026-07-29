from app.config import load_config
from app.job_manager import JobManager
from app.search.demo_searcher import DemoSearcher
from app.agent import JobHunterAgent
from app.logger import setup_logger
from app.scheduler import AgentScheduler


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

    scheduler = AgentScheduler(agent)

    print("=" * 50)
    print("🤖 Job Hunter AI")
    print("=" * 50)

    scheduler.start()


if __name__ == "__main__":
    main()
