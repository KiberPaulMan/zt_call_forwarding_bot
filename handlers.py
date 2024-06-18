import os
from dotenv import find_dotenv, load_dotenv
from aiogram import types, Router, F
from aiogram.filters import Command

from keyboards import reply
import mts_api as api
from databook import phonebook, white_users_id
from parse.duty_file_analysis import get_excel_data, parse_excel_data, get_duty

load_dotenv(find_dotenv())

handlers_router = Router()


@handlers_router.message(Command('start'))
async def process_command_start(message: types.Message):
    await message.reply('Добро пожаловать в телеграм бот!', reply_markup=reply.inline_kb1)


@handlers_router.message(F.text)
async def wrong_messages(message: types.Message):
    await message.answer('Хватит писать тут всякую хрень!')


@handlers_router.callback_query(F.data == 'check_status')
async def process_callback_button1(callback_query: types.CallbackQuery):
    response = api.get_status_call_forwarding()
    if response:
        phone = response[0]['productCharacteristic'][0]['value']
        await callback_query.message.answer(
            text=f'Переадресация выполнена на номер: {phone} ({dict(phonebook.values())[phone]})')
    else:
        await callback_query.message.answer(text=f'На данный номер переадресация не установлена')


@handlers_router.callback_query(F.data == 'create_call_forwarding')
async def process_callback_button2(callback: types.CallbackQuery):
    await callback.message.answer('Сделай выбор, чувак!', reply_markup=reply.person_kb1)


@handlers_router.callback_query(F.data == 'show_timetable')
async def process_callback_button3(callback: types.CallbackQuery):
    await callback.message.answer('Выберите тип расписания:', reply_markup=reply.timetable_kb1)


@handlers_router.callback_query(F.data.in_(phonebook.keys()))
async def process_callback_redirection(callback: types.CallbackQuery):
    response = api.create_call_forwarding(phonebook[callback.data][0])
    if response['status_code'] == 202:
        await callback.message.answer(f'Переадресация на номер {phonebook[callback.data]} выполнена успешна!')
    else:
        await callback.message.answer('Ошибка на сервере! \nПереадресация не выполнена!')


@handlers_router.callback_query(F.data.in_(['all', 'self']))
async def process_callback_show_timetable(callback: types.CallbackQuery):
    out_data = ''
    user_id = callback.from_user.id
    username = [key for key, value in white_users_id.items() if value == user_id][0]

    path = os.getenv('FILE_PATH')

    if not path:
        await callback.message.answer('Файл с дежурствами не найден!')

    ex_data = get_excel_data(path)
    person_data = parse_excel_data(ex_data)

    if callback.data == 'self':
        if username not in phonebook.keys():
            await callback.message.answer('Вас нет в списке пользователей графика дежурств!')
        else:
            out_data = get_duty(person_data, username)
            await callback.message.answer(out_data, parse_mode='HTML')
    elif callback.data == 'all':
        for username in phonebook.keys():
            out_data += f'{get_duty(person_data, username)}\n\n'
        await callback.message.answer(out_data, parse_mode='HTML')


@handlers_router.message()
async def access_users(message: types.Message):
    if message.from_user.id not in white_users_id.values():
        await message.reply('У вас нет прав доступа к этому боту!')
    else:
        await message.reply('Добро пожаловать в телеграм бот!', reply_markup=reply.inline_kb1)
