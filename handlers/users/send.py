from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu import *
from loader import dp, db

MANUAL = "<b>❓Botda qanday qilib pul ishlayman?</b>\n" \
         "— Botga do'stlaringizni taklif qiling va har bir yangi taklif qilgan do'stlaringiz uchun pullik mukofotlarga ega bo'ling.\n\n" \
         "<b>❓Pulni qanday qilib olish mumkin?</b>\n" \
         "— Botda ishlagan pullaringizni telefon raqamingizga chiqarib olishingiz mumkin. (HUMANS raqamlariga to'lab berilmaydi!)\n\n" \
         "<b>👥 Referal qachon aktiv xolatga o'tadi?</b>\n" \
         "— Siz chaqirgan do'stingiz bizning homiylar kanaliga a'zo bo'lganidan so'ng sizning referalingiz hisoblanadi va sizning balansingizga pul tushadi!\n\n" \
         "<i>✅ To'lovlar soni cheklanmagan, xohlaganingizcha shartlar bajaring va pul ishlang!</i>"

TARIX = "<b>Botimiz haqiqatdan ham to'lab beradi. ✅</b>\n\n<i>Quyidagi kanal orqali to'lovlar tarixini kuzatib borishingiz mumkin👇</i>\nhttps://t.me/+Q6TsT4YXvXplZDUy"


@dp.message_handler(text="Balans 💰")
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    id_send = db.select_user(id=user_id)
    for idsend in id_send:
        sql_id = idsend[1]
        await message.reply(text=f"<b>💰Hisobingiz: <code>{sql_id}</code> so'm</b>\n"
                                 f"<b>👥Taklif qilgan do'stlaringiz: <code>{db.count_users(user_id)}</code> odam</b>\n"
                                 f"<b>📱Hisob raqamingiz: <code>+{idsend[2]}</code></b>\n",reply_markup=kb.main())

@dp.message_handler(text="Qo'llanma 📄")
async def bot_start(message: types.Message):
    await message.reply(text=MANUAL,reply_markup=kb.manual())

@dp.message_handler(text="To'lovlar tarixi 🧾")
async def bot_start(message: types.Message):
    await message.reply(text=TARIX, disable_web_page_preview=True)