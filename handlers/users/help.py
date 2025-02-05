from aiogram import types
from aiogram.filters import Command

from loader import dp


@dp.message(Command('help'))
async def bot_help(message: types.Message):
    text = """Botdan foydalanish uchun python kodini botga yuboring va natijani oling, ushbu botda input() funksiyasi ishlamaydi,uning o'rniga ixtiyoriy qiymat kiritib kodingizni to'ldiring."""
    
    await message.answer(text)