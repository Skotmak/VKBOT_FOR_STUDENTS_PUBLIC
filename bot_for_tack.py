# -*- coding: utf8 -*-
import vk_api
import datetime
import pytz
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType




result = 0
fn = 0 # first number of result
sn = 0 # second number of result
a = 1 # переменная для общего бесконечного цикла работы программы
g = 0 # переменная для дебага ожидания

tz_nairobi = pytz.timezone("Africa/Nairobi")
now = datetime.datetime.now(tz_nairobi)


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

def parity_of_the_week():
    '''
    функция определения чётности недели
    '''
    nums = int(datetime.datetime.utcnow().isocalendar()[1]) # 1 выбираем для определения номера недели
    global sn
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
    if (result == 10 or result == 11 or result == 20 or result == 21 or result == 30 or result == 40 or result == 41 or result == 50 or result == 51 or result == 60 or result == 61): # условие отправки сообщения тогда,когда нужно. если у вас каждый день занятия, то уберите это условие и оставье только строчку "sender(id, dict_of_schedule[result])" 
        sender(id, dict_of_schedule[result]) # отправка сообщения из словаря на основе полученной переменной result. Для отправки сообщения нужно вставить в "id" ваш id беседы
    else:
        print("Сегодня занятий нет")


# процесс авторизации
vk_session = vk_api.VkApi(token = 'your_token') # вставьте ваш токен группы
longpoll = VkBotLongPoll(vk_session, your_id_group) # сюда вставьте id группы в "your_id_group"
print(id, "1") # дебаг после авторизации

parity_of_the_week()
sel_num_from_dict()
print(now)

print("------") # дебаг завершения работы программы №1
