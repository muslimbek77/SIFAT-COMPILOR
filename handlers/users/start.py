from aiogram import types
from aiogram.filters import CommandStart
from data.config import ADMINS
from loader import *

@dp.message(CommandStart())
async def start_command(message: types.Message):
    user_info = await bot.get_chat(message.from_user.id)
    try:
        db.add_user(full_name=message.from_user.full_name,telegram_id=message.from_user.id) #foydalanuvchi bazaga qo'shildi
        await bot.send_message(chat_id=-ADMINS[0], text=f"""
🆕 Yangi foydalanuvchi!
🆔 Foydalanuvchi ID: {message.from_user.id}
📛 Foydalanuvchi: {message.from_user.full_name}  
📍 Foydalanuvchining BIO-si: {user_info.bio}
➖➖➖➖➖➖➖➖➖➖➖
🖐Jami: {db.count_users()[0]}""")
        await message.answer(text="Assalomu alaykum, botdan foydalanish uchun python codini botga yuboring.")
    except:
        await message.answer(text="Assalomu alaykum, botdan foydalanish uchun python codini botga yuboring.")