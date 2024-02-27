from aiogram import types


from loader import dp, bot

from aiogram.utils.deep_linking import get_start_link





@dp.message_handler(text="Pul ishlash 💸")
async def Money(message: types.Message):
    user_id =message.from_user
    link = await get_start_link(user_id.id)
    bot_get = await bot.get_me()
    await message.answer("<b>✅ «Axcha Pul» konkursi rasmiy boti.</b>\n\n"
                         f"🎈<a href='{user_id.url}'>{message.from_user.first_name}</a> do'stingizdan unikal havola-taklifnoma.\n\n"
                         f"<b>👇 Boshlash uchun bosing:</b>\n"
                         f"{link}",disable_web_page_preview=True,reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", switch_inline_query=f"{user_id.id}")))

@dp.inline_handler()
async def referals(inline_query: types.InlineQuery):
    user_id =inline_query.from_user
    link = await get_start_link(user_id.id)
    bot_get = await bot.get_me()
    text = f"<b>✅ «Axcha Pul» konkursi rasmiy boti.</b>\n\n"\
           f"🎈<a href='{user_id.url}'>{inline_query.from_user.first_name}</a> do'stingizdan unikal havola-taklifnoma.\n\n"\
           f"📣 <a href='{'https://t.me/+Q6TsT4YXvXplZDUy'}'>{'<b>«About Me : Portfolio»</b>'}</a> kanalining rasmiy botiga do'stlaringizni taklif qiling va kuniga 100.000 so'mdan ko'proq pul toping!\n\n" \
           f"<b>👇 Boshlash uchun bosing:</b>\n"\
           f"{link}"

    input_content = types.InputTextMessageContent(text,disable_web_page_preview=True)
    inl = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("✅ Boshlash ✅", url=f"{link}"))
    referal = types.InlineQueryResultArticle(
        id='01',
        thumb_url=None,
        title="Do'stlarga yuborish 📲",
        description="Do'stlarga yuborish uchun shu yerni bosing",
        input_message_content=input_content,
        reply_markup=inl,
    )
    lis = [referal]
    msg = await inline_query.answer(results=lis, cache_time=1)