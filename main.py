import telebot
from datetime import datetime
import random

# Вставь сюда свой токен
bot = telebot.TeleBot("8072658630:AAFafvZi8EF0Qkjjzacv0lfkB5W9A1zHwUg")

# Храним дату последней попытки для каждого пользователя
users = {}

@bot.message_handler(commands=['start'])
def handle_start(message):
    args = message.text.split()
    user_id = message.chat.id
    today = datetime.now().strftime("%Y-%m-%d")

    if len(args) > 1 and args[1] == "promo":
        if users.get(user_id) == today:
            bot.send_message(user_id, "Вы уже получали промокод сегодня. Попробуйте снова завтра!😬")
        else:
            promo = random.choices(
                ["LUCKY5", "LUCKY10", "LUCKY15", "LUCKY20"],
                weights=[10, 20, 40, 30]
            )[0]
            users[user_id] = today
            bot.send_message(user_id, f"Поздравляем!🎉 Ваш промокод: <b>{promo}</b>", parse_mode="HTML")
    else:
        bot.send_message(user_id, "Привет! Нажмите кнопку в канале, чтобы получить промокод 🎁")

print("✅ Бот запущен...")
bot.polling()
