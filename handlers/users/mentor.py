from aiogram import types
from keyboards.inline.callback_data import course_callback,  mentor_callback, Ict_callback
from keyboards.inline.Inlinebutton import course_button
from keyboards.inline.web_mentor import w_mentor
from keyboards.inline.Mobile_mentor import m_mentor
from keyboards.inline.Deskop_mentor import d_mentor
from keyboards.inline.Computer_graphics_mentor import g_mentor
from keyboards.inline.Computer_science_mentor import s_mentor
from keyboards.inline.sistem_mentor import a_mentor
from aiogram.types import CallbackQuery
from loader import dp


@dp.callback_query_handler(mentor_callback.filter(item_name='mentor_Web_programming'))
async def mentor_web(call:CallbackQuery):
    await call.message.answer('Siz Web programming bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=w_mentor)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(mentor_callback.filter(item_name='mentor_Mobil_programming'))
async def mentor_mobile(call:CallbackQuery):
    await call.message.answer('Siz Mobil programming bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=m_mentor)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(mentor_callback.filter(item_name='mentor_Desktop_programming'))
async def mentor_desktop(call:CallbackQuery):
    await call.message.answer('Siz Desktop programming bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=d_mentor)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(mentor_callback.filter(item_name='mentor_Computer_graphics'))
async def mentor_graphics(call:CallbackQuery):
    await call.message.answer('Siz Computer graphics bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=g_mentor)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(mentor_callback.filter(item_name='mentor_Computer_science'))
async def mentor_science(call:CallbackQuery):
    await call.message.answer('Siz Computer science bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=s_mentor)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(mentor_callback.filter(item_name='mentor_System_Administration_(Cisco)'))
async def mentor_sistem(call:CallbackQuery):
    await call.message.answer('Siz Computer science bo`limini tanladingiz.\nBo`limlardan birini tanlang.',reply_markup=a_mentor)
    await call.message.delete()
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=course_button)
    await call.answer()