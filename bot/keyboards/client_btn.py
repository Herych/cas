from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot.load_all import _

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_('Де ви знаходитесь? 📍'))
        ],
        [
            KeyboardButton(text=_('Як нас знайти')),
            KeyboardButton(text=_('Поширені запитання❓')),
        ],
        [
            KeyboardButton(text=_('Співпраця')),
        ],
    ],
    resize_keyboard=True
)

faq_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_('Дізнатись розклад')),
            KeyboardButton(text=_('Вартість занять'))
        ],
        [
            KeyboardButton(text=_('Групи для початківців')),
            KeyboardButton(text=_('Індивідуальне заняття'))
        ],
        [
            KeyboardButton(text=_('Я не розуміюсь у напрямках'))
        ],
        [
            KeyboardButton(text=_('Хочу знати більше')),
            KeyboardButton(text=_('Вернутись назад🔙'))
        ]
    ],
    resize_keyboard=True
)

direction_of_dance = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_('Парні'))
        ],
        [
            KeyboardButton(text=_('Сольні'))
        ],
        [
            KeyboardButton(text=_('Вернутись назад🔙'))
        ]
    ],
    resize_keyboard=True
)

cooperation = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=_('Оренда залу💃🕺')),
            KeyboardButton(text=_('Вернутись назад🔙'))
        ]
    ],
    resize_keyboard=True
)
