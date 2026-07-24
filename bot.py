import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)

TOKEN = "8669392718:AAE7sunjmHwF23F379mCZqQHOO1DmZuSL1U"

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎁 Открыть подарок",
                    web_app=WebAppInfo(
                        url="https://nuriddinovaferuza641-tech.github.io/Gunel-love/"
                    ),
                )
            ]
        ]
    )

    await message.answer(
        """🌸 Привет, мое золотце... ❤️

Сегодня я хочу подарить тебе не просто подарок.

Я сделал маленький мир, который посвящен только тебе.

В нем собраны мои мысли, теплые слова и самые дорогие для меня воспоминания.

Котя, нажми на кнопку ниже и позволь мне еще раз сказать, как сильно ты для меня значишь. 💖""",
        reply_markup=keyboard,
    )


async def main():
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
