from time import sleep
import json
import emoji
from random import choice
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup,\
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
# t.me/WallEeeeee_bot
gun = KeyboardButton("gun")
sponge = KeyboardButton("sponge")
fire = KeyboardButton("fire")
scissors = KeyboardButton("scissors")
rock = KeyboardButton("rock")
lightning = KeyboardButton("lightning")
devil = KeyboardButton("devil")
dragon = KeyboardButton("dragon")
water = KeyboardButton("water")
air = KeyboardButton("air")
paper = KeyboardButton("paper")
wolf = KeyboardButton("wolf")
tree = KeyboardButton("tree")
man = KeyboardButton("man")
snake = KeyboardButton("snake")
women = KeyboardButton("women")
dinamite = KeyboardButton("dinamite")
nuke = KeyboardButton("nuke")
alien = KeyboardButton("alien")
bowl = KeyboardButton("bowl")
moon = KeyboardButton("moon")
cockroach = KeyboardButton("cockroach")
monkey = KeyboardButton("monkey")
axe = KeyboardButton("axe")
sun = KeyboardButton("sun")

game = ["sponge", "fire", "scissors", "rock", "gun", "lightning", "devil",
        "dragon", "water", "air", "paper", "wolf", "tree", "man", "snake",
        "women", "dinamite", "nuke", "alien", "bowl", "moon", "cockroach",
        "monkey", "axe", "sun"] # список всіх варіантів у грі


markup4 = ReplyKeyboardMarkup().add(
                                                          water, air, paper, tree,
                                                          snake,
                                                          bowl, moon,
                                                          monkey, axe, cockroach)
markup4.row(sponge, fire, scissors,rock,lightning, devil, dragon)
markup5 = ReplyKeyboardMarkup().row(sponge, fire, scissors, rock,
                                                          moon,
                                                          )
markup5.row(axe, sun)
markup5.row(devil, dragon, water, air, paper)
markup5.insert(alien)
markup5.row(wolf, tree, dinamite, nuke)
markup5.row(monkey, bowl)
markup5.row(gun, lightning, cockroach, man)
markup5.row(snake, women)
markup_big = ReplyKeyboardMarkup()

markup_big.add(
    lightning, gun, alien, cockroach, man, wolf
)
markup_big.insert(paper)
markup_big.row(
    axe, sun, snake, devil, nuke, women
)

markup_big.row(fire, bowl)
markup_big.add(moon, monkey)
markup_big.insert(dinamite)
markup_big.insert(tree)
markup_big.insert(KeyboardButton("axe"))
markup_big.row(wolf, dragon, rock, water, air)
buider = ReplyKeyboardMarkup()
buider.add(sponge, fire, scissors, rock,
               gun, lightning, devil,dragon,
               water, air, paper,wolf, tree,
               man, snake, women, dinamite,
               nuke, alien, bowl, moon,
               cockroach, monkey, axe, sun)

TOKEN = "5865107717:AAF4_fDiFHT5PODyzV-6CLQxolvp86lhKbY"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['setdefault'])
async def process_default_command(message: types.Message):
    await message.reply("Default size", reply_markup=buider)

@dp.message_handler(commands=['help']) # команда хелп
async def helping(message:types.message):
    await message.reply(emoji.emojize("<b>You can use these commands</b> :globe_showing_Europe-Africa::"
                        "\n<b>/play</b> :alien_monster: - <i>to start play</i>"
                        "\n<b>/resize2</b> - <i>you can resize your keyboard with line up</i>"
                        "\n<b>/resize3</b> - <i>resize with rows</i> "
                        "\n<b>/resize4</b> - <i>resize all together</i>"
                        "\n<b>/setdefault</b> - <i>set all setings</i>"
                        "\n/<b>rm</b> - <i>remove keyboard</i>(<s>but you can back it</s>)"
                        "\n<b>/showkeyboard</b> - <i>shows your keyboard</i> "
                        "\n<b>/allposiblevariants</b> - <i>you will see all variants in this game</i>"), parse_mode=types.ParseMode.HTML)

@dp.message_handler(commands=['showkeyboard'])
async def process_showing_command(message: types.Message):
    await message.reply("Your keyboard", reply_markup=buider)

@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Clear message templates", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands="resize2")
async def process_resize2_command(message: types.Message):
    await message.reply("Line up buttons", reply_markup=markup4.row(women, dinamite, nuke, man,
                                                                    alien, wolf, gun))

@dp.message_handler(commands=['resize3'])
async def process_resize3_command(message: types.Message):
    await message.reply("Add rows of buttons", reply_markup=markup5)

@dp.message_handler(commands=['resize4'])
async def process_hi7_command(message: types.Message):
    await message.reply("All variants together", reply_markup=markup_big)

inline_btn_1 = InlineKeyboardButton('gun', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton("sun", callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton("nuke", callback_data='btn3')
inline_btn_4 = InlineKeyboardButton("alien", callback_data='btn4')
inline_btn_5 = InlineKeyboardButton("fire", callback_data='btn5')
inline_btn_6 = InlineKeyboardButton("dragon", callback_data="btn6")
inline_btn_7 = InlineKeyboardButton("dinamite", callback_data="btn7")
inline_btn_8 = InlineKeyboardButton("axe", callback_data="btn8")
inline_btn_9 = InlineKeyboardButton("wolf", callback_data="btn9")
inline_btn_10 = InlineKeyboardButton("rock", callback_data="btn10")
inline_btn_11 = InlineKeyboardButton("devil", callback_data="btn11")
inline_btn_12 = InlineKeyboardButton("women", callback_data="btn12")
inline_btn_13 = InlineKeyboardButton("man", callback_data="btn13")
inline_btn_14 = InlineKeyboardButton("cockroach", callback_data="btn14")
inline_btn_15 = InlineKeyboardButton("monkey", callback_data="btn15")
inline_btn_16 = InlineKeyboardButton("bowl", callback_data="btn16")
inline_btn_17 = InlineKeyboardButton("moon", callback_data="btn17")
inline_btn_18 = InlineKeyboardButton("lighting", callback_data="btn18")
inline_btn_19 = InlineKeyboardButton("water", callback_data="btn19")
inline_kb_full.row(inline_btn_11, inline_btn_12, inline_btn_13, inline_btn_14, inline_btn_15)
inline_kb_full.row(inline_btn_16, inline_btn_17, inline_btn_18, inline_btn_19)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_19, inline_btn_18)
inline_kb_full.row(inline_btn_10, inline_btn_6, inline_btn_7, inline_btn_8, inline_btn_9)
inline_kb_full.insert(InlineKeyboardButton("Send bot to my friend", switch_inline_query=''))

@dp.message_handler(commands=['allposiblevariants'])
async def process_command_2(message: types.Message):
    await message.reply("Sending all possible buttons (<b>Beta</b>)", reply_markup=inline_kb_full, parse_mode=types.ParseMode.HTML)

@dp.message_handler(commands=["start"]) # команда старт
async def process_messaging(message: types.message):
    Last_name = message.from_user.last_name
    First_name = message.from_user.first_name
    user_id = message.from_user.id
    print(f"User {message.from_user.full_name}:"
          f"\n  Name - {First_name}"
          f"\n  Last name - {Last_name}"
          f"\n  User id - {user_id}")
    user = {"Name" : First_name,
                   "Last_name" : Last_name,
                   "User id" : user_id}
    with open("data.json", "a") as f:
        json.dump(user, f)
    start = 0
    if start == 0:
        await message.reply(emoji.emojize("Hi! \nMy name is Wall-E :robot:"
                                          "\nHere you can play stone🗿, paper📰: and scissors:scissors:(a little bit more variants)"
                                          "\nPress /help to see what commands you can use!"))
        int(start) + 1
    elif start > 0:
        await message.reply("You already have an account, enter /help")



@dp.message_handler(commands="play")
async def start_play(messege:types.Message):
    messegeF = "stone, paper and scissors, Good luck!"
    await messege.reply(f"You are going to play {messegeF}")

@dp.message_handler(commands=None)
async def winner(messege: types.Message):
    wins = 0
    botChoise = choice(game)
    if messege.text == "gun" and botChoise == "gun": # gun
        await messege.answer("DRAW!!!")
    if (messege.text == "gun") and botChoise in ("rock", "axe", "fire", "snake", "monkey", "women",
                                               "men", "tree", "sun", "cockroach", "wolf", "scissors"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results...")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        wins += 1
        statistics = {"Name" : messege.from_user.full_name,
                      "Wins" : wins}
        print(statistics)
        with open("data.json", "w") as f:
            json.dump(statistics, f)

        await upload_message.delete()
        await messege.answer(emoji.emojize(f"<b>{messege.text.title()}</b> shoots <b>{botChoise.title()}</b>\n"
                             f"\nPlayer wins"), parse_mode=types.ParseMode.HTML)

    if messege.text=="dinamite" and (botChoise=="dinamite"): # dinamite
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "dinamite") and botChoise in ("rock", "scissors", "axe", "fire", "snake", # перевіряєм чи повертає True
                                    "monkey", "women", "men", "tree", "gun", "cockroach", "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(f"<b>{messege.text.title()}</b> explodes💥 <b>{botChoise.title()}</b>"
                             f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text=="nuke" and (botChoise=="nuke "): # nuke
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "nuke") and botChoise in ( "rock", "scissors", "axe", "fire", "snake",
                                    "monkey", "women", "men", "tree", "gun", "dinamite", "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> incinerates☢ <b>{botChoise.title()}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text=="lightning" and (botChoise=="lightning"): # lighting
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "lightning") and botChoise in ("rock", "scissors", "axe", "fire", "snake",
                                    "monkey", "women", "men", "nuke", "gun", "dinamite", "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(2)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> melts⚡ <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "devil" and (botChoise == "devil"): # devil
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "devil") and botChoise in ("rock", "scissors", "axe", "fire", "snake",
                                                                   "monkey", "women", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> eats😈 <b>{botChoise}</b>"
                                      f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "dragon" and (botChoise == "dragon"): # dragon
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "dragon") and botChoise in ("rock", "scissors", "axe", "fire", "snake",
                                                                   "monkey", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b>🐉 breathes <b>{botChoise}</b>"
                                      f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "alien" and (botChoise == "alien"): # alien
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "alien") and botChoise in ("rock", "scissors", "axe", "fire", "snake",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> eliminates🔫 <b>{botChoise}</b>"
                                      f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "water" and (botChoise == "water"): # water
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "water") and botChoise in ("rock", "scissors", "axe", "fire", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> waves🌊 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "bowl" and (botChoise == "bowl"): # bowl
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "bowl") and botChoise in ("rock", "scissors", "water", "fire", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b>🥣 splashes💦 <b>{botChoise.title()}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "air" and (botChoise == "air"): # air
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "air") and botChoise in ("rock", "bowl", "water", "fire", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> freezes🥶 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "moon" and (botChoise == "moon"): # moon
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "moon") and botChoise in ("rock", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> terrifies👻 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "paper" and (botChoise == "paper"): # paper
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "paper") and botChoise in ("rock", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> encases <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "sponge" and (botChoise == "sponge"): # sponge
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "sponge") and botChoise in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> intrigues <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "wolf" and (botChoise == "wolf"): # wolf
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "wolf") and botChoise in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "sponge", "dinamite",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> runs away💨 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "cockroach" and (botChoise == "cockroach"): # cockroach
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "cockroach") and botChoise in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> eats🍴 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "tree" and (botChoise == "tree"): # tree
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "tree") and botChoise in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> shelters🏡 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "man" and (botChoise == "man"): # man
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "man") and botChoise in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> slays🔪 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "women" and (botChoise == "women"): # women
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "women") and botChoise in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> friends🤝 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "monkey" and (botChoise == "monkey"): # monkey
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "monkey") and botChoise in ("paper", "bowl", "water", "air", "alien",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> cheates🥴 <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "snake" and (botChoise == "snake"): # snake
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "snake") and botChoise in ("paper", "bowl", "water", "air", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> bites <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "axe" and (botChoise == "axe"): # axe
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "axe") and botChoise in ("paper", "bowl", "snake", "air", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> chops <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "scissors" and (botChoise == "scissors"): # scissors
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "scissors") and botChoise in ("paper", "axe", "snake", "air", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> cuts <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "fire" and (botChoise == "fire"): # fire
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "fire") and botChoise in ("paper", "axe", "snake", "scissors", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> burns <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "sun" and (botChoise == "sun"): # sun
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "sun") and botChoise in ("paper", "axe", "snake", "scissors", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "fire"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> warms <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

    if messege.text == "rock" and (botChoise == "rock"): # sun
        await messege.answer("DRAW!!!")
    if (messege.text.lower() == "rock") and botChoise in ("sun", "axe", "snake", "scissors", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "fire"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{messege.text.title()}</b> crushes <b>{botChoise}</b>"
                                  f"\nPlayer wins", parse_mode=types.ParseMode.HTML)

# початок логіки бота
 # gun
    if (botChoise == "gun") and messege.text.lower() in ("rock", "axe", "fire", "snake", "monkey", "women",
                                               "men", "tree", "sun", "cockroach", "wolf", "scissors" ):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(f"<b>{botChoise.title()}</b> shoots <b>{messege.text.title()}</b>"
                             f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "dinamite") and messege.text.lower() in ("rock", "scissors", "axe", "fire", "snake", # перевіряєм чи повертає True
                                    "monkey", "women", "men", "tree", "gun", "cockroach", "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(f"<b>{botChoise.title()}</b> explodes <b>{messege.text.title()}</b>"
                             f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "nuke") and messege.text.lower() in ( "rock", "scissors", "axe", "fire", "snake",
                                    "monkey", "women", "men", "tree", "gun", "dinamite", "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> incinerates <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "lightning") and messege.text.lower() in ("rock", "scissors", "axe", "fire", "snake",
                                    "monkey", "women", "men", "nuke", "gun", "dinamite", "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(2)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> melts <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "devil") and messege.text.lower() in ("rock", "scissors", "axe", "fire", "snake",
                                                                   "monkey", "women", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> eats <b>{messege.text.title()}</b>"
                                      f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "dragon") and messege.text.lower() in ("rock", "scissors", "axe", "fire", "snake",
                                                                   "monkey", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> breathes <b>{messege.text.title()}</b>"
                                      f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "alien") and messege.text.lower() in ("rock", "scissors", "axe", "fire", "snake",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> eliminates <b>{messege.text.lower()}</b>"
                                      f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "water") and messege.text.lower() in ("rock", "scissors", "axe", "fire", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> blesses <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "bowl") and messege.text.lower() in ("rock", "scissors", "water", "fire", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> splashes <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise== "air") and messege.text.lower() in ("rock", "bowl", "water", "fire", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> freezes <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "moon") and messege.text.lower() in ("rock", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "sun"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> freezes <b>{messege.text.lower()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "paper") and messege.text.lower() in ("rock", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> encases <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "sponge") and messege.text.lower() in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "gun", "dinamite",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> intrigues <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "wolf") and messege.text.lower() in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "sponge", "dinamite",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> outrans <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "cockroach") and messege.text.lower() in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "nuke", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> eats <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "tree") and messege.text.lower() in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "lighting", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> shelters <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "man") and messege.text.lower() in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "devil", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> slays <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "women") and messege.text.lower() in ("paper", "bowl", "water", "air", "alien",
                                                                   "dragon", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> friends <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "monkey") and messege.text.lower() in ("paper", "bowl", "water", "air", "alien",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> cheates <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "snake") and messege.text.lower() in ("paper", "bowl", "water", "air", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> bites <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "axe") and messege.text.lower() in ("paper", "bowl", "snake", "air", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> chops <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "scissors") and messege.text.lower() in ("paper", "axe", "snake", "air", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> cuts <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "fire") and messege.text.lower() in ("paper", "axe", "snake", "scissors", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "moon"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> burns <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "sun") and messege.text.lower() in ("paper", "axe", "snake", "scissors", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "fire"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> warms <b>{messege.text.title()}</b>"
                                  f"\nBot wins", parse_mode=types.ParseMode.HTML)

    if (botChoise == "rock") and messege.text.lower() in ("sun", "axe", "snake", "scissors", "monkey",
                                                                   "women", "tree", "tree", "cockroach", "sponge", "wolf",
                                                                   "fire"):
        upload_message = await bot.send_message(chat_id=messege.chat.id, text="loading results")
        sleep(1)
        for i in range(11):
            await upload_message.edit_text(text=f"{i}0%")
        sleep(1)
        await upload_message.delete()
        await messege.answer(text=f"<b>{botChoise.title()}</b> crushes <b>{messege.text.title()}</b>"
                                  f"\nbot wins", parse_mode=types.ParseMode.HTML)



executor.start_polling(dp)
