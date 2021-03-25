# -*- coding: utf8 -*-
import vk_api
import datetime
import time
import pytz
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


result = 0
fn = 0 # первая цифра переменной result
sn = 0 # вторая цифра переменной result
a = 1 # переменная для общего бесконечного цикла работы программы
g = 0 # переменная для дебага ожидания

tz_nairobi = pytz.timezone("Africa/Nairobi") #  этот часовой пояс похож на московский
now = datetime.datetime.now(tz_nairobi)
today8am = now.replace(hour=17, minute=10) # переменная запланированого времени

# объявление словаря, 0 - чётная неделя   1 - не чётная неделя, первая цифра соответствует дню недели. заполните вместо "*" так как вам нужно согласно вашему расписанию
dict_of_schedule = {
    10 : '*',
    11 : '*', 
    20 : '*', 
    21 : '*', 
    30 : '*', 
    31 : '*', 
    40 : '*', 
    41 : '*', 
    50 : '*', 
    51 : '*', 
    60 : '*', 
    61 : '*', 
    70 : '*', 
    71 : '*'
    } 


def sender(id, text):
    '''
    функция отправки сообщений
    '''
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text , 'random_id' : 0})

def time_check(now, today8am, g):
    '''
    проверка и сравнение времени и выбор отправляемого сообщения
    '''
    if (now == today8am): # сравнение настоящего времени с запланированым
        parity_of_the_week()
        sel_num_from_dict()
        print("ухожу спать на 23 часа 59 минут (86340 секунд)") # 23:58  (86280 секунд) 23:59 (86340 секунд)
        time.sleep(86340) # уход в сон до следующего дня
        g = 0
    else: 
        print("попробую ещё раз через 60 секунд", ' + ', g)
        g +=1
        time.sleep(60) # метод оптимизации для сокращения количества итераций 

def parity_of_the_week():
    '''
    функция определения чётности недели
    '''
    nums = int(datetime.datetime.utcnow().isocalendar()[1]) # 1 выбираем для определения номера недели
    if (nums % 2) == 0:
        sn = 0
        return sn
 
    if (nums % 2) != 0:
        sn += 1
        return sn

def sel_num_from_dict():
    '''
    функция выбора слова из словаря на основе дня недели
    '''
    num_of_week = int(datetime.datetime.utcnow().isocalendar()[2]) # 2 для выбора номеня дня в неделе
    fn = (num_of_week) * 10
    result = fn + sn
    print(dict_of_schedule[result], ' !end!') # дебаг функции
    if (result == 10 or result == 11 or result == 20 or result == 21 or result == 30 or result == 40 or result == 41 or result == 50 or result == 51 or result == 60 or result == 61): # условие отправки сообщения тогда,когда нужно. если у вас каждый день занятия, то уберите это условие и оставье только строчку 
        sender(id, dict_of_schedule[result]) # отправка сообщения из словаря на основе полученной переменной result
    else:
        print("Сегодня занятий нет")

# процесс авторизации
vk_session = vk_api.VkApi(token = 'your_token') # впишите ваш токен из группы
longpoll = VkBotLongPoll(vk_session, your_id_group) # вместо "your_id_group" вставьте ваш id группы где вы брали токен
print('authorization is ok!') # дебаг после авторизации

for event in longpoll.listen(): # операция получения id беседы многоразовая
    
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat: # ивент для чата
            id = event.chat_id # переменная id беседы
            msg = event.object.message['text'].lower() # все введёные буквы переписываются в нижний регистр
            print(id, "2") # дебаг №2 для операции получения id беседы

            if msg == 'привет бот': # проверка получения стартового сообщения
                sender(id, 'привет, ребята!') # ответное сообщение
                print(id, "3") # дебаг №3 для операции получения id беседы

    while a == 1: # бесконечный цикл работы программы
        # 3 дебага
        print(now)
        print(today8am)
        print("---")
        time_check(now, today8am, g)
            
    print("ок") # дебаг завершения работы программы