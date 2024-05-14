from aiogram import types
import requests
from loader import dp
from aiogram import F
import html


# Echo bot
@dp.message(F.text)
async def bot_echo(message: types.Message):
    url = "https://emkc.org/api/v2/piston/execute"
    payload = {"language": "python3", "files": [message.text], "stdin": "", "version": "3"}
    request = requests.post(url, data=payload)
    json_obj = request.json()
    response = json_obj.get('run')
    res = response.get('stdout')
    text = f"<b>Natija</b>:\n{res}"
    if len(res)>3000:
        for i in range(0,len(text),3000):
                t = "<code>" + text[i:i+3000] + "</code>" 
                await message.answer(t,parse_mode="HTML")
    if res:
        await message.answer(text, parse_mode="HTML")
    else:
         err = response.get('stderr').split(",")[-1]
         err = "<code>"+html.escape(err)+"</code>"
         res = "<b>Xatolik</b>:\n"+err
         
         await message.answer(res, parse_mode="HTML")
         

