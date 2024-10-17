
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

# Токен вашего бота
api = "__"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Класс состояний пользователя
class UserState(StatesGroup):
    age = State()  # Состояние для возраста
    growth = State()  # Состояние для роста
    weight = State()  # Состояние для веса

# Функция для запроса возраста
@dp.message_handler(text='Calories')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
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

# Старт бота
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет! Напиши "Calories", чтобы рассчитать норму калорий.')

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
