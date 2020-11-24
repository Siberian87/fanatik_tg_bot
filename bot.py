import config
import logging
from sqlighter import session, User
from query import get_db_info

from aiogram import Bot, Dispatcher, executor, types
from parser import get_news, get_last_3_news


logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("""Привет. Это новостной бот сайта Fanat1k.ru\n
                        Воспользуйся командами /getnews или /last3news""")


@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    users_id = get_db_info(message.from_user.id)
    if users_id == True:
        await message.answer("Вы уже подписаны.")
    else:
        user_id = User(user_id = message.from_user.id)
        session.add(user_id)
        session.commit()
        await message.answer("Вы подписались на канал.")    
       

@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    users_id = get_db_info(message.from_user.id)
    if users_id == False:
        await message.answer("Вы и так не подписаны.")
    else:
        for row in session.query(User).order_by(User.user_id==message.from_user.id):
            session.delete(row)
            session.commit()
        await message.answer("Вы успешно отписались.")    
    
    
@dp.message_handler(commands=['getnews'])
async def getnews(message: types.Message):
    await message.answer(get_news('http://fanat1k.ru'))


@dp.message_handler(commands=['last3news'])
async def message(message: types.Message):
    news_3 = get_last_3_news('http://fanat1k.ru')
    for i in news_3:
        await message.answer(i)   


if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)