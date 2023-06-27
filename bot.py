import telebot
import config
import audio_recover as au

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start'])
def message_hi(message):
    sticker = open('hello.tgs', 'rb')
    bot.send_sticker(message.chat.id, sticker)
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name}!')

@bot.message_handler(content_types=['voice'])
def transcript(message):
    file_id = message.voice.file_id
    filename = au.download_file(bot, file_id)
    text = au.recognize_speach(filename)
    bot.reply_to(message, text)

bot.polling(none_stop=True)