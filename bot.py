# Пишем значса бота.
# Импортим логгирование, и самописные настройки.
import logging
import settings
# Импортируем Updater из либы питона
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Основное логгирование в файл бот.лог,и уровень  ИНФО и выше
logging.basicConfig(filename='bot.log', level=logging.INFO)


# Словарь с проксей
PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME,
                                  'password': settings.PROXY_PASSWORD}}


# Функция приветствия бота.
def greet_user(update, context):
    print('Вызван старт. /start')
    print(update)
    update.message.reply_text('Дароува Дядь!')


# Функция разговора бота
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


# пишем функцию для запуска тг бота.
def main():
    # Создаем тг бота, и передаем ему апишку для работы
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    # Используем диспетчер, mybot.dispatcher
    # чтобы при наступлении события вызывалась наша функция.
    dp = mybot.dispatcher
    # Добавляем обработчик который будет реагировать на команду Старт
    # И вызывать функцию.
    dp.add_handler(CommandHandler("start", greet_user))
    # Добавляем обработчие реагирующий на текстовые сообщения.
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    # Запись с логгировании что бот стартовал.
    logging.info('Стартуем!!!')

    # Отправляем бота в телегу за сообщениями
    mybot.start_polling()

    # Запуск бота. Работает до принудительной остановки.
    mybot.idle()


# Если этот файл вызвали python3 bot.py
# то этот main будет вызван.
# Если из эттого файла чтото импортировали, то этот блок вызван не будет.
if __name__ == '__main__':
    main()
