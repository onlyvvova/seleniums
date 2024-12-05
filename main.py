import telebot 
import random
from telebot import types
bot = telebot.TeleBot('7307140786:AAHSTuY801nt4OQwAcVHF1mLIx_LUMKpMYA')

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name},тебя приветствует бот WSZE!')

@bot.message_handler(commands=['ecology'])
def ecology(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll = types.KeyboardButton("Викторина")
    save_eco = types.KeyboardButton("Советы")
    kb.row(poll, save_eco)
    bot.send_message(message.from_user.id,'Выберите кнопку',reply_markup=kb)

# Список опросов
polls = [
    {
        'question': 'Что нужно делать для сохранения экологии?',
        'options': ['Не мусорить и не делать костры в неположенных местах', 'Рубить деревья', 'Выбрасывать мусор где попало'],
        'correct_option_id': 0
    },
    {
        'question': 'Что для нас делает экология?',
        'options': ['Ничего', 'Губит все живое', 'Продлевает жизнь'],
        'correct_option_id': 2
    },
    {
        'question': 'Какие птицы прилетают на юг первыми?',
        'options': ['Воробьи', 'Соловьи', 'Грачи'],
        'correct_option_id': 2
    },
    {
        'question': 'Какая ягода бывает белой, черной, красной?',
        'options': ['Калина', 'Черника', 'Смородина'],
        'correct_option_id': 2
    },
    {
        'question': 'Какая птица круглый год ходит во фраке?',
        'options': ['Пингвин', 'Кулистр', 'Страус'],
        'correct_option_id': 0
    },
    {
        'question': 'Кого называют санитаром леса?',
        'options': ['Волка', 'Дятла', 'Сову'],
        'correct_option_id': 0
    }
]

# Храним состояние пользователя (на каком опросе находится)
user_state = {}

@bot.message_handler(content_types=['text'])
def start_poll(message):
    if message.text == 'Викторина':
        user_state[message.chat.id] = 0  # Начинаем с первого опроса
        send_poll(message.chat.id)
    elif message.text == 'Советы':
        adviсe = random.choice(['Правило трех R: reduce, reuse, recycle', 'Экономь электроэнергию', 'Экономь воду', 'Уменьшай потребление пластика'])
        bot.send_message(message.from_user.id, adviсe)

def send_poll(chat_id):
    index = user_state.get(chat_id, 0)
    if index < len(polls):
        poll = polls[index]
        bot.send_poll(
            chat_id=chat_id,
            question=poll['question'],
            options=poll['options'],
            type='quiz',
            correct_option_id=poll['correct_option_id'],
            is_anonymous=False
        )
    else:
        bot.send_message(chat_id, 'Вы прошли все опросы!')

@bot.poll_answer_handler()
def handle_poll_answer(poll_answer):
    chat_id = poll_answer.user.id
    if chat_id in user_state:
        user_state[chat_id] += 1
        send_poll(chat_id)


bot.polling()