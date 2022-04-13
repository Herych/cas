from aiogram import types

from load_all import dp, bot


@dp.callback_query_handler(text='kizomba')
async def callback_kizomba(callback_query: types.CallbackQuery):
    await callback_query.message.answer_video('BAACAgIAAxkBAAIB0WIKPPV6HdfqBB4P8zsU0wz4-HCGAAJkFwACb8rgS_wIHi2xN4mkIwQ')
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.callback_query_handler(text='bachata')
async def callback_bachata(callback_query: types.CallbackQuery):
    await callback_query.message.answer_video('BAACAgIAAxkBAAICHmIKXpLIQCRcy3X12JEsxE5IfBVAAAK6FQACffmQS4vAbSQCYVViIwQ')
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.callback_query_handler(text='salsa')
async def callback_salsa(callback_query: types.CallbackQuery):
    await callback_query.message.answer_video('BAACAgIAAxkBAAICIGIKX_qO0t7lbl6wuKxni4yiLAxPAAK5FQACffmQS-3sWXkKM0rSIwQ')
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.callback_query_handler(text='reggaeton')
async def callback_reggeton(callback_query: types.CallbackQuery):
    await callback_query.message.answer_video('BAACAgIAAxkBAAICNWIKYsZwXCxgeSAZRURgU557oYWOAALqFgAC2j9QSHAOsBbobjSRIwQ')
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.callback_query_handler(text='Lady Style')
async def callback_lady_style(callback_query: types.CallbackQuery):
    await callback_query.message.answer_video('BAACAgIAAxkBAAICN2IKY1LgxX7rfBP1uSgau_nt76OnAAIfGAACfTNRSEs8WJ1TxDRwIwQ')
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.callback_query_handler(text='bodypositive')
async def callback_lady_style(callback_query: types.CallbackQuery):
    await callback_query.message.answer_video('BAACAgIAAxkBAAICOWIKY7nWpjkUI9jVXDjlltyOueoJAAImGAACfTNRSEKpEAFzUcn7IwQ')
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.callback_query_handler(text='menstyle')
async def callback_men_style(callback_query: types.CallbackQuery):
    await callback_query.message.answer_video('BAACAgIAAxkBAAICO2IKZHSKV31wWVk_nfbf3xv_qJVcAAIrGAACfTNRSN72M-1a-gMOIwQ')
    await bot.answer_callback_query(callback_query_id=callback_query.id)


@dp.callback_query_handler(text='rent_rules')
async def rent(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query_id=callback_query.id)
    await callback_query.message.answer_document(
        document='BQACAgIAAxkBAAIILmIUqYG4G4wPeyB59hU7XxLwRMrmAAKvFwACpZ15SEm8vUPiB5dyIwQ')
