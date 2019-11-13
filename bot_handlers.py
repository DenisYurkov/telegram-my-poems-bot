from bot import *  # Import all my_poems
from messages import *  # Import all message


# We send bot greetings
@bot.message_handler(commands=[START_COMMAND, HELP_COMMAND])
def send_welcome(message):
    bot.reply_to(message, AUHTOR)
    bot.reply_to(message, HELP_MESSAGE)
    bot.reply_to(message, CONTACTS)


# Handles all text messages that match the regular expression
# regexp - enter message if only equal to the value in regexp
@bot.message_handler(regexp=INDEX_POEMS)
def handle_message(message_poems):
    bot.reply_to(message_poems, MY_POEMS)


@bot.message_handler(regexp=FIRST_MEETING)
def first_poems_message(first_poems):
    if FIRST_MEETING.lower():
        with open('poems/Первая встреча.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(first_poems, content)


@bot.message_handler(regexp=FORGET)
def second_poems_message(second_poems):
    if FORGET.lower():
        with open('poems/Забудь.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(second_poems, content)


@bot.message_handler(regexp=EMPTINESS)
def third_poems_message(third_poems):
    if EMPTINESS.lower():
        with open('poems/Пустота.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(third_poems, content)


@bot.message_handler(regexp=MATILDA)
def fourth_poems_message(fourth_poems):
    if MATILDA.lower():
        with open('poems/Матильда.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(fourth_poems, content)


@bot.message_handler(regexp=IF_YOU_LOVE_LET_GO)
def fifth_poems_message(fifth_poems):
    if IF_YOU_LOVE_LET_GO.lower():
        with open('poems/Если любишь, отпусти.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(fifth_poems, content)


@bot.message_handler(regexp=INSPIRATION)
def sixth_poems_message(sixth_poems):
    if INSPIRATION.lower():
        with open('poems/Вдохновение.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(sixth_poems, content)


@bot.message_handler(regexp=SECRET_NOTE)
def seventh_poems_message(seventh_poems):
    if SECRET_NOTE.lower():
        with open('poems/Секретная записка.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(seventh_poems, content)


@bot.message_handler(regexp=CHILDHOOD)
def eighth_poems_message(eighth_poems):
    if CHILDHOOD.lower():
        with open('poems/Детство.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(eighth_poems, content)


@bot.message_handler(regexp=UNBEARABLE_LONGING)
def ninth_poems_message(ninth_poems):
    if UNBEARABLE_LONGING.lower():
        with open('poems/Невыносимая тоска.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(ninth_poems, content)


@bot.message_handler(regexp=WHY)
def tenth_poems_message(tenth_poems):
    if WHY.lower():
        with open('poems/Зачем.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(tenth_poems, content)


@bot.message_handler(regexp=LOST_FRIENDSHIP)
def eleventh_poems_message(eleventh_poems):
    if LOST_FRIENDSHIP.lower():
        with open('poems/Потерянная дружба.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(eleventh_poems, content)


@bot.message_handler(regexp=ON_THE_RIVER_BANK)
def twelfth_poems_message(twelfth_poems):
    if ON_THE_RIVER_BANK.lower():
        with open('poems/На берегу реки.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(twelfth_poems, content)


@bot.message_handler(regexp=IN_HEAVEN)
def thirteenth_poems_message(thirteenth_poems):
    if IN_HEAVEN.lower():
        with open('poems/На небесах.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(thirteenth_poems, content)


@bot.message_handler(regexp=FAREWELL_NOTE)
def fourteenth_poems_message(fourteenth_poems):
    if FAREWELL_NOTE.lower():
        with open('poems/Прощальная записка.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(fourteenth_poems, content)


@bot.message_handler(regexp=CITY_OF_THE_DEAD)
def fifteen_poems_message(fifteen_poems):
    if CITY_OF_THE_DEAD .lower():
        with open('poems/Город мертвецов.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(fifteen_poems, content)


@bot.message_handler(regexp=ON_THE_ROAD)
def sixteen_poems_message(sixteen_poems):
    if ON_THE_ROAD.lower():
        with open('poems/В дороге.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(sixteen_poems, content)


@bot.message_handler(regexp=THOUGHTS_IN_MY_HEAD)
def seventeen_poems_message(seventeen_poems):
    if THOUGHTS_IN_MY_HEAD.lower():
        with open('poems/Мысли в голове.txt') as f_obj:
            content = f_obj.read()
            bot.reply_to(seventeen_poems, content)


if __name__ == "__main__":
    bot.polling(none_stop=True)
