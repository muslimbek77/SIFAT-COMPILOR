from aiogram.types import InputFile
import asyncio, sys, logging
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

async def sertificat(full_name):
    img = Image.open("sertifikat.png")
    draw = ImageDraw.Draw(img)
    txt = full_name
    fnt = ImageFont.truetype("roboto2.ttf", 80)
    draw.text((1000-len(txt)*20, 600), txt, font=fnt, fill=(0, 0, 0))

    description = """
        Ushbu sertifikat Zumar Education o'quv markazi tomonidan python dasturlash 
            tilidan topshiriqlarni alo darajada yakunlaganingiz uchun berildi.
    """
    fnt2 = ImageFont.truetype("roboto2.ttf", 40)
    draw.text((200, 800), description, font=fnt2, fill=(0, 0, 0))
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer.read()
