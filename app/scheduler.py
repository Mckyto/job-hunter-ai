import schedule
import time
import logging


class AgentScheduler:

    def __init__(self, agent):
        self.agent = agent

    def run_job(self):

        logging.info("Pornire rulare programata")

        added = self.agent.run()

        logging.info(
            f"Rulare terminata. Joburi noi: {added}"
        )

        print(f"\n✅ Joburi noi adăugate: {added}\n")

    def start(self):

        print("⏰ Scheduler pornit")
        print("Agentul rulează automat conform programării.\n")

        # Rulează imediat la pornire
        self.run_job()

        # Apoi rulează din oră în oră
        schedule.every(1).hours.do(
            self.run_job
        )

        while True:

            schedule.run_pending()

            time.sleep(60)