from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Update, CallbackQuery

from data.config import kanal
from data.tekshirish import tekshir
from filters import IsGuest
from handlers.users.ref_sistem import *
from keyboards.default.menu import *
from loader import dp, db, bot
from aiogram.utils.deep_linking import decode_payload

from utils.db_api.sqlite import is_user_in_db


@dp.message_handler(text="Statistika 📊")
async def Money(message: types.Message):
    user_id =message.from_user
    await message.answer(f"💳 To'lab berilgan jami summa: 90487000 so'm")


# @dp.message_handler(CommandStart())
# async def bot_start(m : types.Message):
#     if is_user_in_db(m.from_user.id) < 1:
#         argument = m.get_args()
#         if (argument is not None) and (argument.isdigit() == True) and (is_user_in_db(argument)) == 1:
#             db.add_user_to_db(id=m.from_user.id, ref_father=argument)
#             db.update_user_balance(balance=REF_BONUS, id=argument)
#             await m.reply(START, reply=False, parse_mode='Markdown', reply_markup=kb.main())
#             await bot.send_message(text="Yangi do'stingiz qabul qilindi sizga 2000 sum berildi", chat_id=argument)
#         else:
#             db.add_user_to_db(id=m.from_user.id)
#             await m.reply(START, reply=False, parse_mode='Markdown', reply_markup=kb.main())
#     else:
#         await m.reply(UPDATE, reply=False, parse_mode='Markdown', reply_markup=kb.main())

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if is_user_in_db(message.from_user.id) < 1:
        argument = message.get_args()
        if (argument is not None) and (argument.isdigit() == True) and (is_user_in_db(argument)) == 1:
            db.add_user_to_db(id=message.from_user.id, ref_father=argument)
            db.update_user_balance(balance=REF_BONUS, id=argument)
            await bot.send_message(text=f"Yangi do'stingiz qabul qilindi sizga {REF_BONUS} sum berildi", chat_id=argument)
        user_id = message.from_user.id
        matn = "Botimizdan foydalanish uchun rasmiy kanalimizga <b>obuna bo'ling</b> va <b>Tekshirish</b> tugmasini bosing."
        royxat = []
        dastlabki = True
        for k in kanal:
            holat = await tekshir(user_id=user_id, kanal_id=k)
            dastlabki *= holat

            kanals = await bot.get_chat(k)
            if not holat:
                link = await kanals.export_invite_link()
                button = [InlineKeyboardButton(text=f"{kanals.title}", url=f"{link}")]
                royxat.append(button)
            # royxat.append([InlineKeyboardButton(text="✅ Tekshirish", callback_data="start")])
            if not dastlabki:
                await bot.send_message(chat_id=user_id, text=matn, disable_web_page_preview=True,
                                       reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
                raise CancelHandler()

        try:
            id = message.from_user.id
            nomer = db.select_user(id=id)
            if nomer[4] == message.contact:
                pass
            else:
                await message.answer(
                    f"{message.from_user.first_name}, siz uchun shart tayyor!\n\nBoshlash uchun <b>«Pul ishlash»</b> tugmasini bosing",
                    reply_markup=kb.main())
        except:
            await message.answer(
                "<b>Telefon raqamingizni yuboring.</b> ❗️\n\nRaqamni yuborish uchun pastdagi <b> «Raqamni yuborish 📞»</b>  tugmasini bosing👇",
                reply_markup=kb.contact())

        else:
            db.add_user_to_db(id=message.from_user.id)
            matn = "Botimizdan foydalanish uchun rasmiy kanalimizga <b>obuna bo'ling</b> va <b>Tekshirish</b> tugmasini bosing."
            royxat = []
            dastlabki = True
            user_id = message.from_user.id
            for k in kanal:
                holat = await tekshir(user_id=user_id, kanal_id=k)
                dastlabki *= holat

                kanals = await bot.get_chat(k)
                if not holat:
                    link = await kanals.export_invite_link()
                    button = [InlineKeyboardButton(text=f"{kanals.title}", url=f"{link}")]
                    royxat.append(button)
                # royxat.append([InlineKeyboardButton(text="✅ Tekshirish", callback_data="start")])
                if not dastlabki:
                    await bot.send_message(chat_id=user_id, text=matn, disable_web_page_preview=True,
                                           reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
                    raise CancelHandler()
            try:
                id = message.from_user.id
                nomer = db.select_user(id=id)
                if nomer[4] == message.contact:
                    pass
                else:
                    await message.answer(
                        f"{message.from_user.first_name}, siz uchun shart tayyor!\n\nBoshlash uchun <b>«Pul ishlash»</b> tugmasini bosing",
                        reply_markup=kb.main())
            except:
                await message.answer(
                    "<b>Telefon raqamingizni yuboring.</b> ❗️\n\nRaqamni yuborish uchun pastdagi <b> «Raqamni yuborish 📞»</b>  tugmasini bosing👇",
                    reply_markup=kb.contact())
    else:
        matn = "Botimizdan foydalanish uchun rasmiy kanalimizga <b>obuna bo'ling</b> va <b>Tekshirish</b> tugmasini bosing."
        royxat = []
        dastlabki = True
        user_id = message.from_user.id
        for k in kanal:
            holat = await tekshir(user_id=user_id, kanal_id=k)
            dastlabki *= holat

            kanals = await bot.get_chat(k)
            if not holat:
                link = await kanals.export_invite_link()
                button = [InlineKeyboardButton(text=f"{kanals.title}", url=f"{link}")]
                royxat.append(button)
            # royxat.append([InlineKeyboardButton(text="✅ Tekshirish", callback_data="start")])
            if not dastlabki:
                await bot.send_message(chat_id=user_id, text=matn, disable_web_page_preview=True,
                                       reply_markup=InlineKeyboardMarkup(inline_keyboard=royxat))
                raise CancelHandler()
        try:
            id = message.from_user.id
            nomer = db.select_user(id=id)
            if nomer[4] == message.contact:
                pass
        except:
            await message.answer(
                f"{message.from_user.first_name}, siz uchun shart tayyor!\n\nBoshlash uchun <b>«Pul ishlash»</b> tugmasini bosing",
                reply_markup=kb.main())

@dp.message_handler(content_types=['contact'])
async def phone_number(message: types.Message):

    id = message.contact.user_id
    phone_usm = message.contact.phone_number
    try:
        db.update_user_number(id=id,
            number=phone_usm)
    except:
        pass
    await message.answer(f"{message.from_user.first_name}, siz uchun shart tayyor!\n\nBoshlash uchun <b>«Pul ishlash»</b> tugmasini bosing", reply_markup=kb.main())

@dp.callback_query_handler(text="start")
async def bot_echo(message: CallbackQuery):
    user_id = message.from_user.id
    try:
        id = message.message.from_user.id
        nomer = db.select_user(id=id)
        if nomer[4] == message.message.contact:
            pass
        else:
            await bot.send_message(chat_id=user_id, text=f"{message.from_user.first_name}, siz uchun shart tayyor!\n\nBoshlash uchun <b>«Pul ishlash»</b> tugmasini bosing",reply_markup=kb.main())
    except:
        await bot.send_message(chat_id=user_id,
            text="<b>Telefon raqamingizni yuboring.</b> ❗️\n\nRaqamni yuborish uchun pastdagi <b> «Raqamni yuborish 📞»</b>  tugmasini bosing👇",
            reply_markup=kb.contact())

