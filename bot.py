import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)
from aiogram.exceptions import (
    TelegramForbiddenError,
    TelegramRetryAfter,
    TelegramNetworkError,
    TelegramAPIError,
)

# ==========================
# НАСТРОЙКИ
# ==========================

TOKEN = "8669392718:AAE7sunjmHwF23F379mCZqQHOO1DmZuSL1U"

WEBAPP_URL = "https://nuriddinovaferuza641-tech.github.io/Gunel-love/"

START_TEXT = """
🌸 Привет, мое золотце... ❤️

Сегодня я хочу подарить тебе не просто подарок.

Я сделал маленький мир,
который посвящён только тебе.

В нём собраны мои мысли,
тёплые слова
и самые дорогие воспоминания.

Нажми на кнопку ниже. 💖
"""

# ==========================
# ЛОГИ
# ==========================

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

# ==========================
# BOT
# ==========================

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ),
)

dp = Dispatcher()


# ==========================
# START
# ==========================

@dp.message(CommandStart())
async def start(message: Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎁 Открыть подарок",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )

    try:
        await message.answer(
            START_TEXT,
            reply_markup=keyboard,
        )

    except TelegramForbiddenError:
        logger.warning(
            "Пользователь %s заблокировал бота",
            message.from_user.id,
        )

    except TelegramRetryAfter as e:
        logger.warning("FloodWait %s секунд", e.retry_after)
        await asyncio.sleep(e.retry_after)

    except TelegramAPIError:
        logger.exception("Ошибка Telegram API")

    except Exception:
        logger.exception("Неизвестная ошибка")


# ==========================
# ЗАПУСК
# ==========================

async def polling():

    while True:

        try:
            logger.info("Бот запущен")

            await dp.start_polling(
                bot,
                allowed_updates=dp.resolve_used_update_types(),
            )

        except TelegramNetworkError:
            logger.warning("Нет соединения. Повтор через 5 сек.")
            await asyncio.sleep(5)

        except Exception:
            logger.exception("Критическая ошибка. Перезапуск через 5 сек.")
            await asyncio.sleep(5)

        finally:
            try:
                await bot.session.close()
            except Exception:
                pass


# ==========================
# MAIN
# ==========================

async def main():
    await polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")