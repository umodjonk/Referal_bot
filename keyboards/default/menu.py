from aiogram import types

class Keyboards:
    def main(self):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        referal = types.KeyboardButton("Pul ishlash 💸")
        balans = types.KeyboardButton("Balans 💰")
        solve = types.KeyboardButton("Pul yechish 💳")
        history = types.KeyboardButton("To'lovlar tarixi 🧾")
        Manual = types.KeyboardButton("Qo'llanma 📄")
        statiska = types.KeyboardButton("Statistika 📊")
        menu.add(referal),menu.add(balans,solve),menu.add(history)
        return menu.add(Manual,statiska)

    def contact(self):
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        contact = types.KeyboardButton("Raqamni yuborish 📞",request_contact=True)
        return menu.add(contact)

    def manual(self):
        menu = types.InlineKeyboardMarkup()
        ADMIN = types.InlineKeyboardButton("Dasturchi",url="https://t.me/+Q6TsT4YXvXplZDUy")
        return menu.add(ADMIN)
kb = Keyboards()