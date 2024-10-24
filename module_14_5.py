from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from crud_functions import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InputFile


api = "6771557547:AAEXxGE1gvzmrJS45Czni4tTNNTyZ1ZpkVA"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

initiate_db()
products = get_all_products()

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton(text='Купить'))
main_kb.add(KeyboardButton(text='Рассчитать норму калорий'))
main_kb.add(KeyboardButton(text='Формулы расчёта'))
main_kb.add(KeyboardButton(text='Регистрация'))


# Инлайн-кнопки продуктов
product_kb = InlineKeyboardMarkup()
product_kb.add(
    InlineKeyboardButton(text='Product1', callback_data='product1'),
    InlineKeyboardButton(text='Product2', callback_data='product2'),
    InlineKeyboardButton(text='Product3', callback_data='product3'),
    InlineKeyboardButton(text='Product4', callback_data='product4')
)

# Класс состояний пользователя
class UserState(StatesGroup):
    age = State()  # Состояние для возраста
    growth = State()  # Состояние для роста
    weight = State()  # Состояние для веса

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

# Основное меню
@dp.message_handler(commands=['start'])
async def main_menu(message: types.Message):
    await message.answer('Привет, я бот для расчета калорий для поддержания веса! Выберите опцию:', reply_markup=main_kb)

@dp.message_handler(text='Регистрация')
async def sign_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя.")
        return
    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = int(message.text)
    data = await state.get_data()
    username = data['username']
    email = data['email']

    # Добавляем пользователя в базу данных
    add_user(username, email, age)

    await message.answer(f"Регистрация завершена! Добро пожаловать, {username}.")
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message: types.Message):
    products = get_all_products()  # Получаем все продукты из базы данных

    for product in products:
        product_title = product[1]
        product_description = product[2]
        product_price = product[3]
        product_image_path = product[4]  #

        # Отправляем локальное изображение
        image = InputFile(product_image_path)
        await bot.send_photo(chat_id=message.chat.id, photo=image)

        # Отправляем описание продукта
        await message.answer(f"Название: {product_title} | Описание: {product_description} | Цена: {product_price}₽")

    await message.answer("Выберите продукт для покупки:", reply_markup=product_kb)

@dp.callback_query_handler(lambda call: call.data.startswith('product'))
async def send_confirm_message(call: types.CallbackQuery):
    product_name = call.data
    await call.message.answer(f"Вы успешно приобрели {product_name.capitalize()}!")
    await call.answer()

# Обработка нажатия кнопки с формулами
@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формулы расчёта: Формула Миффлина-Сан Жеора...')

# Функция для запроса возраста через инлайн-кнопки
@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

# Функция для запроса роста
@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост (в сантиметрах):')
    await UserState.growth.set()

# Функция для запроса веса
@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес (в килограммах):')
    await UserState.weight.set()

# Функция для расчета нормы калорий
@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=float(message.text))  # Вес как float
    data = await state.get_data()  # Получаем данные пользователя

    # Извлечение данных из состояния
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    # Формула Миффлина - Сан Жеора для мужчин
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5

    # Отправляем результат пользователю
    await message.answer(f"Ваше количество калорий для поддержания веса: {round(bmr, 2)} ккал/день.")

    # Завершаем машину состояний
    await state.finish()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
