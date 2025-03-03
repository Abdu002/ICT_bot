from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import mentor_graphics_mavzu

graphics_programming_mavzu = {
"Adobe Photoshop":"g_course_Adobe_Photoshop",
"Adobe Illustration":"g_course_Adobe_Illustration",
"Corel DRAW":"g_course_Corel_DRAW",
"3D Max, V-ray":"g_course_3D Max_V-ray",
"AutoCAD":"g_course_AutoCAD",
}

g_mentor = InlineKeyboardMarkup(row_width=2)
for key,value in graphics_programming_mavzu.items() :
    python = InlineKeyboardButton(text=key, callback_data=mentor_graphics_mavzu.new(item_name=value))
    g_mentor.insert(python)  

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
g_mentor.insert(back_button)