import os
import telebot

# Токен вашего бота получается у @BotFather в Telegram
TOKEN = os.getenv("BOT_TOKEN", "9223025693:AAHBYIDP6m-DG1PW5SLb8g7RLqdEu5wUqa0
")
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
  # Пример поста с аналитикой
  text = (
      "📊 **Прогноз на матч**\n\n⚽ **Команда А — Команда Б**\n🏆 Турнир: Лига"
      " Чемпионов\n💡 Прогноз: Победа команды А с форой (0)\n📈 Коэффициент:"
      " 1.85\n\n💬 **Аналитика:** Команда А находится в отличной форме и имеет"
      " серию из 4 побед подряд на домашнем стадионе."
  )
  bot.send_message(message.chat.id, text, parse_mode="Markdown")


if __name__ == "__main__":
  bot.infinity_polling()
