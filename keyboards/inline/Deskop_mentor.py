from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import mentor_desktop_mavzu

desktop_programming_mavzu = {
"C++":"d_course_c+",
"C#":"d_course_c#",
}

d_mentor = InlineKeyboardMarkup(row_width=2)
for key,value in desktop_programming_mavzu.items() :
    python = InlineKeyboardButton(text=key, callback_data=mentor_desktop_mavzu.new(item_name=value))
    d_mentor.insert(python)  

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
d_mentor.insert(back_button)