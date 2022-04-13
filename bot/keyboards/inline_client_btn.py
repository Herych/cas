from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.load_all import _

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=_('Кізомба'), callback_data='kizomba')
        ],
        [
            InlineKeyboardButton(text=_('Бачата'), callback_data='bachata')
        ],
        [
            InlineKeyboardButton(text=_('Сальса'), callback_data='salsa')
        ]
    ]
)

choice_solo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Reggaeton', callback_data='reggaeton')
        ],
        [
            InlineKeyboardButton(text='Lady Style', callback_data='Lady Style')
        ],
        [
            InlineKeyboardButton(text='BodyPositive&Latina (40+)', callback_data='bodypositive')
        ],
        [
            InlineKeyboardButton(text='Men Style', callback_data='menstyle')
        ]
    ]
)

rent_place = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=_('Правила оренди (PDF)'), callback_data='rent_rules')
        ],
    ]
)
