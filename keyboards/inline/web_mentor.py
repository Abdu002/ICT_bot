from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import mentor_web_mavzu 

Web_programming_mentor = {
"Frontend ":"w_mentor_Frontend",
"Backend ":"w_mentor_Backend",
"Framework ":"w_mentor_Framework",

}

w_mentor = InlineKeyboardMarkup(row_width=2)
for key,value in Web_programming_mentor.items() :
    python = InlineKeyboardButton(text=key, callback_data=mentor_web_mavzu.new(item_name=value))
    w_mentor.insert(python)  

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
w_mentor.insert(back_button)