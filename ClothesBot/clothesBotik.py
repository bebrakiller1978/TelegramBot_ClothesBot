from black import Sized
import telebot;
from telebot import types
import json

bot = telebot.TeleBot('5068289217:AAGeuJKqN2bYezjE1bUx4i0nuz78dbvE_iQ');

categories=['Одежда','Обувь','Аксессуары']
clothes=['Верхняя одежда','Худи и свитшоты','Футболки и майки','Штаны',"Шорты","Костюмы","Спортивные костюмы","Нижнее белье"]
pants=['Брюки',"Чиносы","Джинсы","Джоггеры","Спортивные штаны"]
setGetSizeFunction=['Ввести размер самостоятельно','Определить размер']
daNet=['Да','Нет']
typeOfSizes = ['Европейский', 'Российский', 'Американский']
genders = ['Мужчина', 'Женщина']
bedros = ['78-84','85-87','88-90','91-93','94-96','97-99','100-102','103-105','106-108','109-111','112-114','115','116-118','118-120','120-122','123-126','127']
colors = ['Черный','Синий','Белый','Бежевый','Красный']
typesOfGeans = ['Прямой крой', 'Skinny', 'Обычный крой', 'Расклешенные']
brands = ['Levi\'s', 'Armani', 'Calvin Klein', 'Gucci', 'Tommy Jeans']
users = {}
translate = {
    'Одежда':'clothes',
    'Штаны':'pants',
    'Джинсы':'geans',
    'Мужчина':'male',
    'Женщина':'female',
    'Европейский':'evro',
    'Российский':'rus',
    'Американский':'USA'
    
}


dial1 = 'Выбери одну из представленных категорий:\n\n(Для выбора категории введите номер рядом с категорией)'
dial2 = 'Я тебя не понимаю. Введи число.'
dial3 = 'Выбери тип размера'
dial4 = 'Выбери пол'
dial5 = 'Выбери размер'
sorry = 'Данная функция находится на этапе разработки. В скором времени она будет доступна.'
dial6 = "Введи обхват бёдер в см"
dial7 = "Хочешь ли ты указать дполнительные критерии для своего элемента одежды?"
dial8 = "Вот что мне удалось по твоим запросам:"
dial9 = 'Хочешь ли ты добавить дополнительные критерии для своей вещи?'
dial10 = 'Выбери цвет'
dial11 = 'Выбери тип'
dial12 = 'Выбери бренд'


def getCat(categories,message,dial='Выбери один из вариантов'):
    keyboard = types.InlineKeyboardMarkup()
    for i in range(len(categories)):
        key_cat = types.InlineKeyboardButton(text=categories[i], callback_data=categories[i])
        keyboard.add(key_cat)
    bot.send_message(message.from_user.id, dial, reply_markup=keyboard )


def getSize(gender,typeOfSize):
    evroSize = []
    with open('dataSize.json', 'r') as j:
        sizes = json.load(j)
    for i in range(len(sizes)):
        size=sizes[i][gender][typeOfSize]
        if (not size in evroSize) and size != '':
            evroSize.append(size)
    return(evroSize)

def setGetSize(call):
    with open('dataSize.json', 'r') as j:
        sizes = json.load(j)
    print(call.data)
    sizes_find = bedros.index(call.data)
    gender = users[call.from_user.id]['gender']
    typeOfSize = users[call.from_user.id]['typeOfSize']
    size = sizes[sizes_find][gender][typeOfSize]
    users[call.from_user.id]['size'] = size
    bot.send_message(call.from_user.id, f'Ваш размер: {size}')


def pjson(items):
    str1 = ''
    for item in items:
        str1 += "Производитель: "+ item['brand'] + " \n\nЦвет: " + item['color'] + ""\
            " \n\nСтоимость: " + str(item['cost']['dollar']) +"$ " + str(item['cost']['rub'])  + " р."\
            "\n\nСсылка: " + item['link'] + "\n\n\n\n"
    return str1

def get_all_shtani():
    fileObject = open("data2.json", "r", encoding = "UTF-8")
    jsonContent = fileObject.read()
    ListOfItem = json.loads(jsonContent)
    str1 = ""
    for item in ListOfItem:
        str1 += pjson(item) + "\n"
    return str1

@bot.message_handler(content_types=['text',])
def get_text_messages(message):
    global users
    global allabai
    if str(message.text).lower() == "/start":
        users[message.from_user.id] = {}
        bot.send_message(message.from_user.id, "Привет, я ClothesBot. Я могу узнать твой размер и подобрать тебе вещи из различных интернет магазинов, учитывая твои предпочтения.")
        bot.send_message(message.from_user.id, "Принцип моей работы прост. Я отправляю тебе список категорий товаров, а ты выбираешь нужную из них.\n \nЧтобы выбрать категорию просто нажми на кнопку с нужной категорией.")
        getCat(categories,message,dial1) 
        allabai = 1
    elif (message.text).isdigit() and allabai == 1:
        users[message.from_user.id]['mincost'] = message.text
        print('gfjgdjkhgdfjk')
        message.text=''
        print(users)
        allabai = 0
        bot.send_message(message.from_user.id, 'Введи верхний порок цены')
        return(allabai)
    elif (message.text).isdigit():
        users[message.from_user.id]['maxcost'] = message.text
        print(users)
        getCat(setGetSizeFunction,message)

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /start.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    try:
        global users
        global a
    #
    #категории
    #
        
        if call.data in categories: 
            users[call.from_user.id]['categories'] = translate[call.data]
            getCat(globals()[f'{translate[call.data]}'],call,dial1)
    #
    #одежда        
    #
        elif call.data in clothes:
            users[call.from_user.id]['clothes'] = translate[call.data]
            getCat(globals()[f'{translate[call.data]}'],call,dial1)
    #
    #штаны
    #
        elif call.data in pants:
            users[call.from_user.id]['pants'] = translate[call.data]
            getCat(daNet,call,dial9)
    #
    #функция доп параметров
    #
    #цвет
        elif call.data == daNet[0]:
            getCat(colors,call,dial10)
        elif call.data == daNet[1]:
            getCat(setGetSizeFunction,call)
    #тип
        elif call.data in colors:
            users[call.from_user.id]['color'] = call.data
            getCat(typesOfGeans,call,dial11)
        elif call.data in typesOfGeans:
            users[call.from_user.id]['type'] = call.data
            getCat(brands, call, dial12)
    #бренд
        elif call.data in brands:
            users[call.from_user.id]['brand'] = call.data
            bot.send_message(call.from_user.id, 'Введи нижний порок цены')
    #цена
    #
    #функция setGetSize
    #
        elif call.data == setGetSizeFunction[0]:
            getCat(genders,call,dial4)
            a = 0
        elif call.data == setGetSizeFunction[1]:
            getCat(genders,call,dial4)
            a = 1
    #
    #выбор пола
    #
        elif call.data in genders:
            users[call.from_user.id]['gender'] = translate[call.data]
            getCat(typeOfSizes,call,dial3)
    #
    #выбор размера
    #
        elif call.data in typeOfSizes and a == 0:
            users[call.from_user.id]['typeOfSize'] = translate[call.data]
            getCat(getSize(users[call.from_user.id]['gender'],users[call.from_user.id]['typeOfSize']),call,dial5)
        elif call.data in typeOfSizes and a == 1:
            users[call.from_user.id]['typeOfSize'] = translate[call.data]
            getCat(bedros,call,dial6)
        elif call.data in bedros:
            setGetSize(call)
            print('=========', call.data, '=========')
        elif call.data in getSize(users[call.from_user.id]['gender'],users[call.from_user.id]['typeOfSize']) or call.data in bedros:
            print('gfgnosafdfsad')
            if call.data in getSize(users[call.from_user.id]['gender'],users[call.from_user.id]['typeOfSize']):
                users[call.from_user.id]['size'] = call.data
            elif call.data in bedros:
                pass
            print(users)
            fileObject = open("data.json", "r", encoding = "UTF-8")
            jsonContent = fileObject.read()
            geans = json.loads(jsonContent)
            items = []
            for gean in geans:
                if gean['size'][users[call.from_user.id]['gender']][users[call.from_user.id]['typeOfSize']] == users[call.from_user.id]['size'] and gean['type'] == users[call.from_user.id]['type'] and gean['color'] == users[call.from_user.id]['color'] and int(users[call.from_user.id]['mincost']) <= int(gean['cost']['rub']) <= int(users[call.from_user.id]['maxcost']) and gean['brand'] == users[call.from_user.id]['brand'] :
                    items.append(gean)
            bot.send_message(call.from_user.id, pjson(items))
            pjson(items)
        if call.data in bedros: 
            if call.data in getSize(users[call.from_user.id]['gender'],users[call.from_user.id]['typeOfSize']):
                users[call.from_user.id]['size'] = call.data
            elif call.data in bedros:
                pass
            print(users)
            fileObject = open("data.json", "r", encoding = "UTF-8")
            jsonContent = fileObject.read()
            geans = json.loads(jsonContent)
            items = []
            for gean in geans:
                if gean['size'][users[call.from_user.id]['gender']][users[call.from_user.id]['typeOfSize']] == users[call.from_user.id]['size'] and gean['type'] == users[call.from_user.id]['type'] and gean['color'] == users[call.from_user.id]['color'] and int(users[call.from_user.id]['mincost']) <= int(gean['cost']['rub']) <= int(users[call.from_user.id]['maxcost']) and gean['brand'] == users[call.from_user.id]['brand'] :
                    items.append(gean)
            bot.send_message(call.from_user.id, pjson(items))
            pjson(items)
    except:
       bot.send_message(call.from_user.id, sorry) 
        
    print(users)




bot.polling(none_stop=True, interval=0) 