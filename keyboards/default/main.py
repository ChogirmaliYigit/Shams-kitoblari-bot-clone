from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

main_markup = ReplyKeyboardMarkup(resize_keyboard=True)
main_markup.row(KeyboardButton(text="đ Buyurtma berish"))
main_markup.row(KeyboardButton(text="đ Savat"), KeyboardButton(text="đĻ Buyurtmalarim"))
main_markup.row(KeyboardButton(text="âšī¸ Biz haqimizda"), KeyboardButton(text="âī¸ Sozlamalar"))
main_markup.row(KeyboardButton(text="âī¸ Fikr qoldirish"))


cart_button = KeyboardButton(text="đ Savat")
clearance_button = KeyboardButton(text="đ Rasmiylashtirish")
back_button = KeyboardButton(text="âŦī¸ Orqaga")
home_button = KeyboardButton(text="đ  Bosh menyu")
clear_button = KeyboardButton(text="đ Tozalash")

cats_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
cats = db.select_cats()
for cat in cats:
    cats_markup.insert(KeyboardButton(text=cat[1]))
cats_markup.add(cart_button, clearance_button)
cats_markup.add(back_button, home_button)


def secondary_cart_markup(cats):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    secondary_cats = db.select_secondary_cats(cat_id=cats[0])
    for cat in secondary_cats:
        markup.insert(KeyboardButton(text=cat[1]))
    markup.add(cart_button, clearance_button)
    markup.add(back_button, home_button)
    return markup


def products_markup(secondary_cat):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    products = db.select_products(secondary_cat_id=secondary_cat[0])
    for product in products:
        markup.insert(KeyboardButton(text=product[1]))
    markup.add(cart_button, clearance_button)
    markup.add(back_button, home_button)
    return markup

amount_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
for i in range(1, 10):
    amount_markup.insert(KeyboardButton(text=str(i)))
amount_markup.add(cart_button, back_button)


def cart_markup(products):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for product in products:
        mahsulot = db.select_product(id=product[-2])
        markup.row(KeyboardButton(text=f"â {mahsulot[1]}"))
    markup.add(back_button, clear_button)
    markup.add(clearance_button)
    return markup

