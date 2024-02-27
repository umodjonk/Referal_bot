from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    argument = message.text
    jbj = argument.isdigit()
    print(jbj)
    txt = message.text
    print(message)
    await message.answer(txt)
