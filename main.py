from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import aemet
import conf_management as ConfMgt
import schedule
import time
import menu_recipe


def start(bot, update):
    message = "Bienvenido al bot de Cora!"
    bot.send_message(chat_id=update.message.chat_id, text=message)


def hello(bot, update):
    greeting = "Hola, {}".format(update.effective_user.username)    
    bot.send_message(chat_id=update.message.chat_id, text=greeting)


def add(bot, update, args):
    result = sum(map(int, args))
    message = "The result is: {}".format(result)
    bot.send_message(chat_id=update.message.chat_id, text=message)


def weather(bot, update):
    ok = False
    result_text = ''

    ok, result_text = aemet.get_weather(ConfMgt.get_aemet_token())

    if not ok:
        bot.send_message(chat_id=update.message.chat_id, text='Error al conectar con AEMET')
    else:
        bot.send_message(chat_id=update.message.chat_id, text=result_text)


def recipe(bot, update):
    """
    reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Ver recetas', callback_data='show_recipes')],
                [InlineKeyboardButton('Receta aleatoria', callback_data='random_recipe')],
                [InlineKeyboardButton('Cancelar', callback_data='cancel')]
            ]
        )
    """
    reply_markup = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Ver recetas', callback_data='show_recipes'),
                    InlineKeyboardButton('Receta aleatoria', callback_data='random_recipe')],
                [InlineKeyboardButton('Adulto comida aleatoria', callback_data='adult_random_lunch'),
                    InlineKeyboardButton('Adulto cena aleatoria', callback_data='adult_random_dinner')],
                [InlineKeyboardButton('Niña comida aleatoria', callback_data='kid_random_lunch'),
                    InlineKeyboardButton('Niña cena aleatoria', callback_data='kid_random_dinner')],
                [InlineKeyboardButton('Cancelar', callback_data='cancel')]
            ]
        )

    bot.send_message(
        chat_id=update.message.chat_id,
        text='¿Qué quieres hacer?',
        reply_markup=reply_markup
        )


def button(bot, update):
    bot.deleteMessage(
        chat_id=update.callback_query.message.chat_id,
        message_id=update.callback_query.message.message_id
        )

    txt_result = ''

    if update.callback_query.data == 'show_recipes':
        txt_result = menu_recipe.Recipe.get_text_recipes()
    elif update.callback_query.data == 'cancel':
        txt_result = 'OK'
    elif update.callback_query.data == 'random_recipe':
        txt_result = menu_recipe.Recipe.get_random_recipe()
    elif update.callback_query.data == 'adult_random_lunch':
        txt_result = menu_recipe.Recipe.get_random_recipe_filtered(is_lunch=True,for_adult=True)
    elif update.callback_query.data == 'adult_random_dinner':
        txt_result = menu_recipe.Recipe.get_random_recipe_filtered(is_dinner=True,for_adult=True)
    elif update.callback_query.data == 'kid_random_lunch':
        txt_result = menu_recipe.Recipe.get_random_recipe_filtered(is_lunch=True,for_kids=True)
    elif update.callback_query.data == 'kid_random_dinner':
        txt_result = menu_recipe.Recipe.get_random_recipe_filtered(is_dinner=True,for_kids=True)

    bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        text=txt_result
        )


def main(bot_token):
    """ Main function of the bot """
    updater = Updater(token=bot_token)
    dispatcher = updater.dispatcher

    # Query handler
    query_handler = CallbackQueryHandler(button)
    dispatcher.add_handler(query_handler)

    # Command handlers
    start_handler = CommandHandler('start', start)
    hello_handler = CommandHandler('hello', hello)
    add_handler = CommandHandler('add', add, pass_args=True)
    weather_handler = CommandHandler('weather', weather)
    recipe_handler = CommandHandler('recipe', recipe)

    # Add the handlers to the bot
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(hello_handler)
    dispatcher.add_handler(add_handler)    
    dispatcher.add_handler(weather_handler)
    dispatcher.add_handler(recipe_handler)

    # Starting the bot
    updater.start_polling()


def envia_telegram(bot_token, id_chat, texto_enviar):
    update = Updater(token=bot_token)
    update.bot.send_message(chat_id=id_chat, text=texto_enviar)


def check_weather():
    ok = False
    result_text = ''

    ok, result_text = aemet.get_weather(ConfMgt.get_aemet_token())

    if not ok:
        envia_telegram(ConfMgt.get_telegram_token(), ConfMgt.get_telegram_group_id(), 'Error al conectar con AEMET')
    else:
        envia_telegram(ConfMgt.get_telegram_token(), ConfMgt.get_telegram_group_id(), result_text)


if __name__ == "__main__":
    main(ConfMgt.get_telegram_token())

    for hour in ConfMgt.get_schedule():
        schedule.every().day.at(hour).do(check_weather)

    while True:
        schedule.run_pending()
        time.sleep(1)
