from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from databook import phonebook


inline_btn_1 = InlineKeyboardButton(text='Проверить статус переадресации', callback_data='check_status')
inline_btn_2 = InlineKeyboardButton(text='Выполнить переадресацию', callback_data='create_call_forwarding')
inline_btn_3 = InlineKeyboardButton(text='Просмотр расписания', callback_data='show_timetable')

inline_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [inline_btn_1],
        [inline_btn_2],
        [inline_btn_3],
    ]
)

person_btn_1 = InlineKeyboardButton(text=list(phonebook.values())[0][1], callback_data=list(phonebook.keys())[0])
person_btn_2 = InlineKeyboardButton(text=list(phonebook.values())[1][1], callback_data=list(phonebook.keys())[1])
person_btn_3 = InlineKeyboardButton(text=list(phonebook.values())[2][1], callback_data=list(phonebook.keys())[2])
# person_btn_4 = InlineKeyboardButton(text=list(phonebook.values())[3][1], callback_data=list(phonebook.keys())[3])

person_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [person_btn_1],
        [person_btn_2],
        [person_btn_3],
    ]
)


timetable_btn_1 = InlineKeyboardButton(text='Общее расписание', callback_data='all')
timetable_btn_2 = InlineKeyboardButton(text='Моё расписание', callback_data='self')

timetable_kb1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [timetable_btn_1],
        [timetable_btn_2],
    ]
)
