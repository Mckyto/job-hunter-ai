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


    def start(self):

        schedule.every(1).hours.do(
            self.run_job
        )

        print("⏰ Scheduler pornit")
        print("Agentul rulează automat conform programării.")


        while True:

            schedule.run_pending()

            time.sleep(60)
