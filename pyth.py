import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update

TOKEN = "8271675134:AAGD2VOfc5tC3k3Utwsday3bRMhY0XCUyto"


async def handle_update(update: Update, bot: Bot):
    if update.message:
        keyboard = [
            [InlineKeyboardButton("обо мне", callback_data="who_am_i")],
            [InlineKeyboardButton("мой телеграмм канал", callback_data="channel")],
            [InlineKeyboardButton("ссылки на соц сети", callback_data="social_links")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await bot.send_message(
            chat_id=update.message.chat_id,
            text="выбери что конкретно ты хочешь узнать:",
            reply_markup=reply_markup,
        )
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        if query.data == "who_am_i":
            await bot.send_message(
                chat_id=query.message.chat_id,
                text="Из увлечений: учусь программировать и работаю над проектами на различные темы:). Очень хочу поступить в МГТУ им. Баумана и сдать ЕГЭ нормально.Сейчас состою в кп гагаринских и гуляю в основном в центре",
            )
        elif query.data == "channel":
            await bot.send_message(
                chat_id=query.message.chat_id(
                    text="мой тгк", url="https://t.me/+vo6PyOUuIt5lYjEy"
                )
            )
        elif query.data == "social_links":
            await bot.send_message(
                chat_id=query.message.chat_id(text="Вк", url="https://vk.com/gizapahx")
            )


async def main():
    bot = Bot(token=TOKEN)
    offset = 0
    while True:
        updates = await bot.get_updates(offset=offset, timeout=10)
        for update in updates:
            await handle_update(update, bot)
            offset = max(offset, update.update_id + 1)
            bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    asyncio.run(main())
