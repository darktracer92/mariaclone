# -*- coding: utf-8 -*-
import telebot

bot = telebot.TeleBot("711433002:AAEKhBxnMRBRCDvTLDTtbL8adFV0AUqJtk4")

@bot.message_handler(commands=['about'])
def about(message):
    msg = "🎩 Hecho por @JuanjoSalvador \n⚒ Repositorio: https://github.com/JuanjoSalvador/maria-bot/ \n❓ Incidencias: https://github.com/JuanjoSalvador/maria-bot/issues/"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=(['status']))
def status(message):
    msg = "Estado: ✅"
    chat_id = message.chat.id
    bot.send_message(chat_id, msg)

@bot.message_handler(func=lambda m: True, content_types=['new_chat_members'])
def welcome(message):
    if message.new_chat_member.username:
        new_member = message.new_chat_member.username
    else:
        new_member = "undefined"
        
    chat_name = message.chat.title
    msg = "¡Bienvenido/a a {}, @{}! Espero que tu estancia sea agradable. No te olvides de leer las normas del grupo.".format(chat_name, new_member)
    chat_id = message.chat.id

    bot.send_message(chat_id, msg)

def main():
    bot.polling()

if "__name__" == "__main__":
    main()
