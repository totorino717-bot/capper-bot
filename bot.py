import os
import threading
from flask import Flask
import telebot

# 1. Запуск микро-сервера Flask для обхода платных ограничений
app = Flask(__name__)


@app.route("/")
def home():
  return "Bot is running!"


def run_web():
  port = int(os.getenv("PORT", 8080))
  app.run(host="0.0.0.0", port=port)


# 2. Логика Telegram-бота
TOKEN = os.getenv("BOT_TOKEN", "ВАШ_ТОКЕН_БОТА")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(
      message,
      "Привет! Я бот-каппер. Здесь будет публиковаться аналитика и прогнозы"
      " матчей.",
  )


@bot.message_handler(commands=["prediction"])
def send_prediction(message):
  text = (
      "📊 **Прогноз на матч**\n\n⚽ **Команда А — Команда Б**\n🏆 Турнир: Лига"
      " Чемпионов\n💡 Прогноз: Победа команды А с форой (0)\n📈 Коэффициент:"
      " 1.85\n\n💬 **Аналитика:** Команда А находится в отличной форме и имеет"
      " серию из 4 побед подряд на домашнем стадионе."
  )
  bot.send_message(message.chat.id, text, parse_mode="Markdown")


if __name__ == "__main__":
  # Запускаем веб-сервер в отдельном потоке
  threading.Thread(target=run_web, daemon=True).start()
  # Запускаем самого бота
  bot.infinity_polling()
