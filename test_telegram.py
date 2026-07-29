from app.notifications.telegram_bot import TelegramBot

bot = TelegramBot()

ok = bot.send_message("✅ Test Job Hunter AI - conexiunea cu Telegram funcționează!")

print("Mesaj trimis:", ok)