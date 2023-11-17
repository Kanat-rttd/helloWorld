from django.core.management.base import BaseCommand
import telebot
from bot.models import User

bot = telebot.TeleBot("6881872826:AAERyruc05V9ql3UNs6Dnj-4s_TQtuj9dPM")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Привет, <strong>{message.from_user.first_name}</strong> ", parse_mode='html')


@bot.message_handler(commands=['users'])
def users(message):
    users = User.objects.all()
    for user in users:
        user_info = f"{user.name}, {user.device}"
        bot.send_message(message.chat.id, user_info)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/start - Поприветствовать пользователя\n/users - Вывод юзеров из базы данных и их устройства')


@bot.message_handler(commands=['add'])
def get_user_name(message):
    bot.send_message(message.chat.id, 'Введите имя пользователя: ')
    bot.register_next_step_handler(message, get_user_device)


def get_user_device(message):
    global user_name
    user_name = message.text
    bot.send_message(message.chat.id, 'Введите ваше устройство')
    bot.register_next_step_handler(message, full_info)


def full_info(message):
    user_device = message.text

    new_user = User(name=user_name, device=user_device)
    new_user.save()

    bot.send_message(message.chat.id, 'Информация была сохранена')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")