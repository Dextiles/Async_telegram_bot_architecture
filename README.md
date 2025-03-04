# Asynchronous Telegram Bot Architecture

[Русский](#архитектура-асинхронного-телеграм-бота) | [English](#asynchronous-telegram-bot-architecture)

## Description
This project is an asynchronous Telegram bot written in Python using the `pyTelegramBotAPI` library. The bot supports infinite polling interaction and has the ability to set default commands.

## Installation
To install and run the bot, follow these steps:

1. Clone the repository:
    ```sh
    git clone <your-repository-url>
    cd <repository-name>
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root of the project and add your Telegram bot token:
    ```env
    BOT_TOKEN="your_token"
    ```
   See the `.env.template` file for more details.

5. Run the bot:
    ```sh
    python main.py
    ```

## Features
- **Asynchronous operation**: The bot works asynchronously, allowing it to handle multiple requests simultaneously.
- **Setting default commands**: When the bot starts, default commands are set, which can be used by users.
- **Infinite polling interaction**: The bot constantly polls the Telegram server for new messages and processes them.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

# Архитектура асинхронного телеграм-бота

[Русский](#архитектура-асинхронного-телеграм-бота) | [English](#asynchronous-telegram-bot-architecture)

## Описание
Этот проект представляет собой асинхронного телеграм-бота, написанного на Python с использованием библиотеки `pyTelegramBotAPI`. Бот поддерживает бесконечное опросное взаимодействие и имеет возможность установки команд по умолчанию.

## Установка
Для установки и запуска бота выполните следующие шаги:

1. Клонируйте репозиторий:
    ```sh
    git clone <URL вашего репозитория>
    cd <название репозитория>
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корне проекта и добавьте в него ваш токен телеграм-бота:
    ```env
    BOT_TOKEN="ваш_токен"
    ```
   Подробнее изучите шаблон файла `.env.template`.

5. Запустите бота:
    ```sh
    python main.py
    ```

## Функционал
- **Асинхронная работа**: Бот работает асинхронно, что позволяет ему обрабатывать несколько запросов одновременно.
- **Установка команд по умолчанию**: При запуске бота устанавливаются команды по умолчанию, которые могут быть использованы пользователями.
- **Бесконечное опросное взаимодействие**: Бот постоянно опрашивает сервер Telegram на наличие новых сообщений и обрабатывает их.

## Лицензия
Этот проект лицензирован по лицензии MIT. Подробности можно найти в файле `LICENSE`.