from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import mentor_science_mavzu

science_programming_mavzu = {
"Windows 7/8/10 da ishlash":"s_course_Windows",
"Office ilovalari":"s_course_Office_ilovalari",
"Kompyuter yig`ish":"s_course_Kompyuter_yig`ish",
"Operatsion tizimlar o`rnatish":"s_course_Operatsion",
"Internetda ishlash":"s_course_Internetda_ishlash",
}

s_mentor = InlineKeyboardMarkup(row_width=2)
for key,value in science_programming_mavzu.items() :
    python = InlineKeyboardButton(text=key, callback_data=mentor_science_mavzu.new(item_name=value))
    s_mentor.insert(python)  

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
s_mentor.insert(back_button)