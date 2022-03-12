from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import mentor_sistem_mavzu

sistem_programming_mavzu = {
"Cisco":"a_course_Cisco",
}

a_mentor = InlineKeyboardMarkup(row_width=2)
for key,value in sistem_programming_mavzu.items() :
    python = InlineKeyboardButton(text=key, callback_data=mentor_sistem_mavzu.new(item_name=value))
    a_mentor.insert(python)  

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
a_mentor.insert(back_button)