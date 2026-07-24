import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
)

from config import BOT_TOKEN

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

    text = (
        "🌸 Привет, мое золотце... ❤️\n\n"
        "Сегодня для тебя есть кое-что особенное.\n\n"
        "Я очень долго готовил этот подарок, потому что хотел, "
        "чтобы ты улыбнулась именно так, как улыбаешься только ты.\n\n"
        "Здесь собраны мои мысли, воспоминания и самые теплые слова, "
        "которые я хотел сказать тебе.\n\n"
        "Поэтому, госпожа... ✨\n"
        "Нажми кнопку ниже и открой свой маленький мир, созданный специально для тебя. 💖"
    )

    await message.answer(text, reply_markup=keyboard)


async def main():
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())