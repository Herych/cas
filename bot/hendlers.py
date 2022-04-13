from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards import choice, choice_solo, rent_place, faq_menu, direction_of_dance, cooperation, start_menu
from text import text_jun_team, text_individual_sessions

from load_all import dp, _, bot
import database

db = database.DBCommands()


@dp.message_handler(CommandStart())
async def register_user(message: Message):
    await db.add_new_user()

    languages_markup = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text='Українська 🇺🇦',
                callback_data='lang_ua')],
            [types.InlineKeyboardButton(
                text='English 🇬🇧',
                callback_data='lang_en')]
        ]
    )
    await message.answer('Привіт, вибери мову, якою з тобою спілкуватися:\n'
                         'Hi, choose a language to communicate with you:', reply_markup=languages_markup)


@dp.callback_query_handler(text_contains='lang')
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    lang = call.data[-2:]
    await db.set_language(lang)
    await call.message.answer(_("Ваша мова була змінена", locale=lang))
    await call.message.answer(_('Для роботи з ботом натисни /menu', locale=lang))


@dp.message_handler(commands=["menu"])
async def main_menu(message: types.Message):
    await message.delete()
    await message.answer(text=(_('Для роботи з ботом, скористайтесь меню:')),
                         reply_markup=start_menu)


@dp.message_handler(text=_('Де ви знаходитесь? 📍'))
async def get_place_command(message: types.Message):
    await message.answer(_('Вітаю {message}! Ми знаходимося у центрі Києва, вул. Жилянська 5-Б,'
                           ' м. Олімпійська. З нами можна '
                           'ewrewr'
                           "зв'язатися за тел. 0970817651 (12:00-20:00), або ж у Telegram "
                           'https://t.me/CasaderitmoAcademy').format(message=message.from_user.first_name))
    await message.answer_location(latitude=50.43354025071111, longitude=30.515333808968762)


@dp.message_handler(text=_('Як нас знайти'))
async def how_find_us(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAIDJGIKi1ldNxXavg-7lRc-8kscB4zKAAKQGQACfTNRSJEC94QaFWT8IwQ')


@dp.message_handler(text=_('Поширені запитання❓'))
async def faq(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               _('Інше питання? ☎️ тел. 0970817651 (12:00-20:00)'), reply_markup=faq_menu)
        await message.delete()
    except Exception:
        await message.reply(_('Спілкування з ботом можливе через ПП, напишіть йому:\n@Casa_test_bot'))


@dp.message_handler(text=_('Дізнатись розклад'))
async def time_sheet(message: types.Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIBkmIKK7IEBwa3ZO9yFTifkZZdRY1oAAJyuTEb95ZRSMTL0GBrzYJAAQADAgADcwADIwQ')


@dp.message_handler(text=_('Вартість занять'))
async def price_lessons(message: types.Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICnmIKaIsulVwunypE6Pi0Qa2MObYgAAIZuzEbfTNRSM4pGqi8ss_uAQADAgADcwADIwQ'
    )


@dp.message_handler(text=_('Групи для початківців'))
async def jun_team(message: types.Message):
    await message.answer(text=f'{text_jun_team}')


@dp.message_handler(text=_('Індивідуальне заняття'))
async def individual_sessions(message: types.Message):
    await message.answer(text=f'{text_individual_sessions}')


@dp.message_handler(text=_('Я не розуміюсь у напрямках'))
async def direction_dance(message: types.Message):
    await message.answer(_(f'Види напрямків: '), reply_markup=direction_of_dance)


@dp.message_handler(text=_('Парні'))
async def dabl_dance(message: types.Message):
    await message.answer(_('Парні види танців: '), reply_markup=choice)


@dp.message_handler(text=_('Сольні'))
async def solo_dance(message: types.Message):
    await message.answer(_('Сольні види танців :'), reply_markup=choice_solo)


@dp.message_handler(text=_("Співпраця"))
async def coop(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               _('Інше питання? ☎️ тел. 0970817651 (12:00-20:00)'), reply_markup=cooperation)
        await message.delete()
    except Exception:
        await message.reply(_('Спілкування з ботом можливе через ПП, напишіть йому:\n@Casa_test_bot'))


@dp.message_handler(text=_('Оренда залу💃🕺'))
async def rent(message: types.Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICx2IKdiNoYZqD8ZbKEBZVLOEkpz9pAAIquzEbfTNRSAU3raIIa4LAAQADAgADcwADIwQ',
        caption=_('Оренда залу при 100% передоплаті. Деталі у "Правилах оренди".'),
        reply_markup=rent_place
    )


@dp.message_handler(text=_("Вернутись назад🔙"))
async def return_to_menu(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               _('Для роботи з ботом, скористайтеся меню:'), reply_markup=start_menu)
        await message.delete()
    except Exception:
        await message.reply(_('Спілкування з ботом можливе через ПП, напишіть йому:\n@Casa_test_bot'))


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=_('Якщо ви не знайшли відповіді на ваше запитання, або все супер! '
                                'І ви хочете записатися на заняття або співпрацювати - напишіть нашому адміністратору '
                                'https://t.me/CasaderitmoAcademy'))
