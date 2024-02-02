import time
import logging
from aiogram.types import InputFile
from datetime import datetime
newdate = datetime.now()
sd = datetime.isoweekday(newdate)
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#dispatcher - ответственен за апдейты, а executor за запуск и связь с ботом и пользователем
TOKEN = '6093208162:AAHJVehSLCu8HyAp0hzfsTOBGvj3MC0j604'
#создаём переменную, в которой записан наш токен, отсылающий к боту
bot = Bot(token=TOKEN)
#привязываем токен к боту(специальная функция)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
#и привязываем диспетчер к боту
#создаём клавиатуру
mar = ReplyKeyboardMarkup(resize_keyboard=True)#one_time_keyboard=True
kn1=KeyboardButton('/help')
kn2=KeyboardButton('❤️')
kn3=KeyboardButton('/day')
mar.add(kn1,kn2,kn3)
iklava = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
ikn1=KeyboardButton('5')
ikn2=KeyboardButton('6')
ikn3=KeyboardButton('7')
ikn4=KeyboardButton('8')
ikn5=KeyboardButton('9')
ikn6=KeyboardButton('10')
ikn7=KeyboardButton('11')
iklava.add(ikn1,ikn2,ikn3,ikn4,ikn5,ikn6,ikn7)
klava =  ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kn=KeyboardButton('/today')
k1=KeyboardButton('/monday')
k2=KeyboardButton('/tuesday')
k3=KeyboardButton('/wednesday')
k4=KeyboardButton('/thursday')
k5=KeyboardButton('/friday')
k6=KeyboardButton('/saturday')
klava.add(kn).add(k1).add(k2).add(k3).add(k4).add(k5).add(k6)
#список команд
scom="""
<b>/help</b> - список команд
<b>/start</b> - начало работы 
<b>/grade</b> - выбор класса
<b>/day</b> - расписание на день"""
@dp.message_handler(commands=['help'])
async def fof(message: types.Message):
    await message.answer(text=scom,parse_mode="HTMl")
    await message.delete()
@dp.message_handler(commands=['start'])
#команда старт, ниже - что нужно делать, если она приходит
#используем async, так как айограм - ассинхронная библиотека, поэтому и заканчиваем функцию не ретурн, а await
async def startik(message: types.Message):
    #message - это то, что нам отправляет пользователь
    user_id = message.from_user.id
    #идентификатор чата с пользователем
    user_name = message.from_user.full_name
    #я знаю кто и что делает и его имя, и даже когда он написал
    logging.info(f'{user_id} {user_name}', time.asctime())
    await message.answer(f"WASSSSSSSSSUP, {user_name} \nвыбири класс:",reply_markup=iklava)
@dp.message_handler(commands=['grade'])
async def startik(message: types.Message, state: FSMContext):
    user_name = message.from_user.full_name
    await message.answer(f"{user_name}, выбири класс:",reply_markup=iklava)
    if message.text == '5'or message.text =='6' or message.text =='7'or message.text =='8'or message.text =='9'or message.text =='10'or message.text =='11':
        if message.text == '5':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\oo.jpg'))
            await bot.send_message(message.from_user.id,text="Ваше расписание на неделю",reply_markup=mar)
            kk = 5
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '6':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 6
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '7':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\oooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 7
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '8':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ooooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 8
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '9':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\oooooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 9
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '10':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ooooooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 10
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '11':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\oooooooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 11
            async with state.proxy() as data:
                data['ref1'] = kk
@dp.message_handler(commands=['day'])
async def day(message: types.Message):
    user_name = message.from_user.full_name
    await message.answer(f"{user_name}, выбери день:",reply_markup=klava)
@dp.message_handler(commands=['today'])
async def sg(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text="Ваше расписание на сегодня", reply_markup=mar)
    async with state.proxy() as data:
        kk = data['ref1']
    if sd == 1:
        if kk == 5:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p11.jpg'))
    elif sd == 2:
        if kk == 5:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v11.jpg'))
    elif sd == 3:
        if kk == 5:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s11.jpg'))
    elif sd == 4:
        if kk == 5:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch11.jpg'))
    elif sd == 5:
        if kk == 5:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt11.jpg'))
    elif sd == 6:
        if kk == 5:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb11.jpg'))
@dp.message_handler(commands=['monday'])
async def sg(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text="Ваше расписание на понедельник", reply_markup=mar)
    async with state.proxy() as data:
        kk = data['ref1']
        if kk == 5:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\p11.jpg'))
@dp.message_handler(commands=['tuesday'])
async def sg(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text="Ваше расписание на вторник", reply_markup=mar)
    async with state.proxy() as data:
        kk = data['ref1']
        if kk == 5:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\v11.jpg'))
@dp.message_handler(commands=['wednesday'])
async def sg(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text="Ваше расписание на среду", reply_markup=mar)
    async with state.proxy() as data:
        kk = data['ref1']
        if kk == 5:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\s11.jpg'))
@dp.message_handler(commands=['thursday'])
async def sg(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text="Ваше расписание на четверг", reply_markup=mar)
    async with state.proxy() as data:
        kk = data['ref1']
        if kk == 5:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ch11.jpg'))
@dp.message_handler(commands=['friday'])
async def sg(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text="Ваше расписание на пятницу", reply_markup=mar)
    async with state.proxy() as data:
        kk = data['ref1']
        if kk == 5:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\pt11.jpg'))
@dp.message_handler(commands=['saturday'])
async def sg(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, text="Ваше расписание на субботу", reply_markup=mar)
    async with state.proxy() as data:
        kk = data['ref1']
        if kk == 5:
            await bot.send_photo(message.from_user.id,photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb5.jpg'))
        if kk == 6:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb6.jpg'))
        if kk == 7:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb7.jpg'))
        if kk == 8:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb8.jpg'))
        if kk == 9:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb9.jpg'))
        if kk == 10:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb10.jpg'))
        if kk == 11:
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\sb11.jpg'))
@dp.message_handler()
async def boje(message: types.Message,state: FSMContext):
    if message.text == '5'or message.text =='6' or message.text =='7'or message.text =='8'or message.text =='9'or message.text =='10'or message.text =='11':
        if message.text == '5':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\oo.jpg'))
            await bot.send_message(message.from_user.id,text="Ваше расписание на неделю",reply_markup=mar)
            kk = 5
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '6':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 6
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '7':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\oooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 7
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '8':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ooooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 8
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '9':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\oooooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 9
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '10':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\ooooooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 10
            async with state.proxy() as data:
                data['ref1'] = kk
        elif message.text == '11':
            await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\oooooooo.jpg'))
            await bot.send_message(message.from_user.id, text="Ваше расписание на неделю", reply_markup=mar)
            kk = 11
            async with state.proxy() as data:
                data['ref1'] = kk
    elif message.text == '❤️':
        await bot.send_sticker(message.from_user.id,
                               sticker="CAACAgIAAxkBAAEICy1kB4qaEEcnrZffxtbOm15Hcz7z6AACAg0AAvoAAUhIpIuZzSYbq2AuBA")
    else:
        return 0
    #await message.answer( "выбири класс:", reply_markup=types.ReplyKeyboardRemove())
    #await message.delete()
    #удаляет сообщение пользователя для того, чтобы не засорять чат
@dp.message_handler(commands=['creator'])
async def je(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=InputFile(r'C:\Users\Acer\OneDrive\Изображения\герыч.jpg'))
#по сути это while True, но выглядит хайповее(мы запускаем этот модуль непосредственно напрямую)
if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)







