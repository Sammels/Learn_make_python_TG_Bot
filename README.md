Проект 1.
Простой учебный телеграмм бот. Что-то типа болванки.

Хз, мб чонить и вырастит из энтого.
У нас в деревне все пишут на эвантом ващем-то питоне.

1. Идеем в телегу.
2. ищем BotFather
3. Регаем нового бота /newbot
4. pip3 install python-telegram-bot[socks]
5. cd Project_1
6. mkdir mybot
7. touch bot.py
------------------------------
Понадобится апдейтер Updater

Updater - Отвечает за коммуникацию с сервером.
-----------------------------------------------------------
Настройки проксей для телеграм бота.
t1.learn.python.ru:1080 login learn password python
t2.learn.python.ru:1080 login learn password python
t3.learn.python.ru:1080 login learn password python

# Словарь с проксей
PROXY = {'proxy_url':'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs':{'username':'learn', 'password':'python'}}

    mybot = Updater("СуперСесюритиПоинт",
          use_context=True, request_kwargs=PROXY
---------------------------------------------------------------------------
1.1. Добавление команды обработки Старт. (/start)

Напишем функционал, чтобы бот реагировал на действия пользователя.
1. Делается обработчик команды старт.
2. У бота есть диспетчер. Кто-то кто занимается адресацией сообщений.

Для обработки команд используется CommandHandler

1.2. Создаем функцию greet_user
Бот вызовет  функцию greet_user, когда пользователь напишет команду /start
или нажмет кнапулю.

def greet_user(update, context):
    print('Вызван старт. /start')

1.3 Наладим обработку, и взаимодействие с пользователем.
Ответ пользователю при помощи <b>update.message.reply_text()</b>
-----------------------------------------
1.4 Если произошла ошибка. Добавляем логгирование.

import logging

После импортирования добавим конфигурирование.
Запишем все сообщения уровня INFO в файл bot.log

Добавим строку конфигурации после импорта и перед настройкой PROXY
logging.basicConfig(filename='bot.log', level=logging.INFO)

Добавим логгирование чтобы бот стартовал.
logging.info("Бот стартовал")
----------------------
1.5 Добавление обработчика текстовых сообщений.
MessageHandler - позволяет обрабатывать все типы сообщений.

from telegram.ext import MessageHandler, Filters

1.6 Добавим обработчик событий в main()
При использовании MessageHandler укажем, что мы хотим реагировать только
на текстовые сообщения - Filters.text

dp.add_handler(MessageHandler(Filters.text, talk_to_me))
---------------------------------------------------------------------------
1.7 Дополнительные улучшения
- Убираем апишечку из бласти видимости
- Заделаем гит репо
- Выложим на гит

1. Делаем Setting

2.
# Если этот файл вызвали python3 bot.py
# то этот main будет вызван.
# Если из эттого файла чтото импортировали, то этот блок вызван не будет.
if __name__ == '__main__':
    main()

3. Го в гит.
В папке проекта
git init
git status

4. Пихаем в Гит игнор все что нужно

повтор 3 шага
