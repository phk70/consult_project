import os
import logging
import telegram
from dotenv import load_dotenv
# import asyncio  # Для теста


# Логирование для отображения в терминале.
logging.basicConfig(level=logging.DEBUG)


async def send_telegram_message(token, chat_id, message, parse_mode="Markdown"):

# Если все верно, то создаем экземпляр бота и отправляем message на определенный token и chat_id.
# parse_mode - стиль отображения (markdown, markdownV2 или html)
    try:
        bot = telegram.Bot(token=token) # type: ignore
        await bot.send_message(chat_id=chat_id, text=message, parse_mode=parse_mode)
        logging.info(f'Сообщение "{message}" отправлено в чат {chat_id}')

# Если что то не так, то выводим ошибку и прерываем.
    except Exception as e:
        logging.error(f"Ошибка отправки сообщения в чат {chat_id}: {e}")
        raise

# Тест отправки
# if __name__ == "__main__":
#     load_dotenv()
#     TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
#     YOUR_PERSONAL_CHAT_ID = os.getenv("YOUR_PERSONAL_CHAT_ID")
#     message = "*Тестовое сообщение*"
#     asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))