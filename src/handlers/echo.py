from aiogram import Router
from aiogram.types import Message


router: Router = Router()


@router.message()
async def process_any_message(message: Message):
    await message.reply(text=message.text)
