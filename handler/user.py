from aiogram import Bot , Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import CommandStart
from environs import Env
from buttons import REG_text
env = Env()
env.read_env()

user_router = Router()

@user_router.message(CommandStart())
async def start(message: Message ):
    
    await message.answer(REG_text)

    
