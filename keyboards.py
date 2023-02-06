from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_fin = KeyboardButton('/final')
btn_agree = KeyboardButton('/agree')
btn_help = KeyboardButton('/help')
btn_start = KeyboardButton('/start')

kb_main_menu.add(btn_start, btn_agree)
kb_main_menu.add(btn_help, btn_fin)
