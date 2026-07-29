import os
import requests
from dotenv import load_dotenv


load_dotenv()


class TelegramBot:

    def __init__(self):

        self.token = os.getenv("TELEGRAM_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")


    def send_message(self, message):

        if not self.token or not self.chat_id:
            print("⚠️ Telegram nu este configurat.")
            return False


        url = (
            f"https://api.telegram.org/"
            f"bot{self.token}/sendMessage"
        )

        data = {
            "chat_id": self.chat_id,
            "text": message
        }


        response = requests.post(
            url,
            data=data
        )


        return response.status_code == 200