import telebot
from telebot import types
import random
items = [
    "Ферменты",
    "Азотистый обмен",
    "Липидный обмен",
    "Витамины",
    "Биологическое окисление",
    "Углеводный обмен",
    "Белковый обмен",
    "Биохимия органов и тканей",
    "Водно-минеральный обмен",
    "Биохимия регуляций",
    "Все сразу"
    ]
item = ''
n = 0
flag = 0
fr = 0

                        #-----------------------------------
questionsf = []
t = []
def empty(s):
                            ans = 1
                            for x in s:
                                if x != ' ':
                                    ans = 0
                                    break
                            return ans 
                            
                        #-------------------------------------------Ввод ферментов
file1 = open('Ферменты.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsf.append(t)
                                t = []
                            else:
                                t.append(line.strip())

file1.close
                        #-------------------------------------------Ввод окисления
questionso = []
file1 = open('Биологическое окисление.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionso.append(t)
                                t = []
                            else:
                                t.append(line.strip())
file1.close
                        #-------------------------------------------Ввод азотистый обмен
questionsa = []
file1 = open('Азотистый обмен.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsa.append(t)
                                t = []
                            else:
                                t.append(line.strip())
file1.close
                        #-------------------------------------------Ввод Белковый обмен
questionsb = []
file1 = open('Белковый обмен.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsb.append(t)
                                t = []
                            else:
                                t.append(line.strip())

file1.close
                        #-------------------------------------------Ввод органы и ткани
questionsor = []
file1 = open('Биохимия органов и тканей.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsor.append(t)
                                t = []
                            else:
                                t.append(line.strip())

file1.close
                        #-------------------------------------------Ввод регуляций
questionsr = []
file1 = open('Биохимия регуляций.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsr.append(t)
                                t = []
                            else:
                                t.append(line.strip())

file1.close
                        #-------------------------------------------Ввод витамин
questionsv = []
file1 = open('Витамины.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsv.append(t)
                                t = []
                            else:
                                t.append(line.strip())

file1.close
                        #-------------------------------------------Ввод Водно-минеральный обмен
questionsw= []
file1 = open('Водно-минеральный обмен.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsw.append(t)
                                t = []
                            else:
                                t.append(line.strip())

file1.close
                        #-------------------------------------------Ввод липидный
questionsl = []
file1 = open('Липидный обмен.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsl.append(t)
                                t = []
                            else:
                                t.append(line.strip())

file1.close
                        #-------------------------------------------Ввод углеводный
questionsu = []
file1 = open('Углеводный обмен.txt', encoding = 'utf-8', mode = 'r')  

while True:
                            # считываем строку
                            line = file1.readline()
                            # прерываем цикл, если строка пустая
                            if not line:
                                break
                            # выводим строку
                            if(empty(line.strip()) == 1):
                                questionsu.append(t)
                                t = []
                            else:
                                t.append(line.strip())

file1.close


bot = telebot.TeleBot('5386839036:AAHjJw2TVMump1U9yC5NCfQ7BvAhsbn8dEQ');
@bot.message_handler(content_types=['text','photo','url'])


def get_text(message):
    global fr;
    global items
    global item
    global flag, n;
    global questionsa, questionsor, questionl,questionr, questionsb, questionsv, questionsw, questionor, questionsb, questionsu, questionso
    f = [ 1,1,4,1,1,2,3,2,1,1,2,1,1,1,1,1,1,1,1,3,1,1  ,1,2,4,2,1,1,2,3,2,2,2,2,1,1,2,2,4,3,3,1,4,1,2,4,4,2,4,3,2,5,5,2,1,3,1,2,4,1,3,1,3,2,2,5,2,4,4,3,3,3,3,2,4,2,]
    o = [ 2,3,1,1,4,4,3,2,3,3,1,1,1,3,4,4,4,3,4,1,2,4,4,2,2,2,2,1,3,1,3,1,1,3,1,1,2,2,2,2,4,1,3,2,1,3,1,4,1,4,3,4,3,2,2,3,3,1,2,3,4,4,4,2,3,1,3,3,3,1,1,1,4,1,3,3,4,4,4,3,1,2,5,4,2,1,5,4,1,2,]
    u = [ 1,1,2,2,2,2,2,1,2,1,1,5,3,3,1,1,1,1,1,4,1,3,1,1,1,3,4,1,1,2,1,1,1,3,1,1,2,3,1,3,4,3,2,1,1,1,1,1,1,1,3,2,1,2,4,4,3,1,1,2,1,1,2,1,2,2,1,2,2,3,2,1,4,4,2,1,2,1,3,3,3,3,3,1,4,3,1,2,3,3,1,3,2,4,1,2,5,1,3,3,5,3,2,3,1,1,5,3,1,1,1,4,3,3,2,2,2,3,1,3,1,1,2,2,2,]
    l = [ 1,3,2,1,4,3,4,2,3,2,1,2,2,4,2,3,2,2,2,1,4,3,3,1,3,1,1,3,2,3,2,3,3,2,1,2,2,3,1,2,3,3,2,1,3,2,3,2,1,2,2,2,2,4,1,5,4,1,2,4,3,1,2,3,2,3,1,1,3,1,5,2,4,1,1,4,3,1,2,4,2,3,1,1,2,2,3,2,4,2,2,2,2,1,3,1,1,1,2,3,2,2,3,2,2,1,2,2,1,4,4,4,2,2,4,2,4,3,5,4,2,2,3,3,1,2,3,2,1,1,4,4,1,]
    b = [ 1,1,3,1,2,4,2,3,3,2,4,1,2,1,2,2,2,2,1,2,2,3,3,1,2,4,2,1,4,1,4,3,3,1,4,2,1,2,4,2,3,4,1,2,1,2,1,1,3,4,2,1,2,2,2,2,4,1,1,2,2,2,3,1,3,3,4,1,2,2,3,3,2,3,2,2,3,2,2,4,3,3,2,3,2,5,1,4,1,2,1,2,3,1,2,1,2,1,1,2,2,2,2,3,2,4,1,1,2,3,1,3,3,1,2,5,3,3,2,2,1,3,3,3,1,1,4,1,4,2,1,1,3,3,4,1,2,1,1,1,1,3,2,3,1,2,1,3,3,2,2,4,3,2,2,4,4,3,3,3,3,2,1,1,3,4,1,3,2,2,1,4,2,3,3,]
    a = [ 4,4,3,3,4,2,4,1,3,1,2,4,1,3,1,4,2,4,4,2,2,2,1,3,2,3,1,4,5,5,2,3,4,3,1,4,1,2,2,1,2,2,2,1,2,3,2,1,3,2,1,2,3,1,2,2,2,1,3,2,1,1,2,2,2,4,2,3,4,2,3,1,2,1,1,2,1,3,2,1,1,2,1,2,3,2,2,3,2,1,4,5,1,2,3,2,2,4,1,3,5,4,6,4,3,2,1,1,4,1,4,1,3,4,4,4,3,3,3,3,1,1,1,3,4,3,1,1,3,]
    v = [ 1,1,1,1,3,3,1,4,3,3,1,3,3,3,2,2,3,3,1,4,3,3,2,2,2,3,1,3,2,2,2,2,1,2,1,1,4,2,1,1,3,3,3,2,1,3,2,2,2,3,3,1,3,3,3,3,3,3,4,2,2,4,4,2,1,1,]
    r = [ 2,1,3,1,1,2,2,1,2,2,1,3,4,1,4,2,4,4,3,4,3,2,3,3,1,4,3,1,1,1,2,2,2,2,1,2,3,1,2,4,1,2,4,2,1,1,1,1,2,1,1,1,3,2,2,1,1,1,3,1,1,3,1,1,3,2,1,1,1,3,3,4,1,1,4,4,1,1,1,4,3,2,2,1,5,3,5,4,4,3,2,3,2,1,4,3,4,5,4,4,1,2,1,1,2,4,4,4,2,3,4,4,1,5,2,2,]
    w = [ 2,3,1,2,1,1,1,2,4,1,1,1,2,3,4,2,1,4,3,2,1,1,1,3,1,1,1,1,2,2,1,2,2,2,2,3,1,]
    or_ = [ 3,1,3,1,4,3,2,1,3,2,3,2,1,2,2,2,1,1,1,3,1,1,1,1,3,2,3,1,3,3,3,3,2,4,1,3,1,1,2,3,1,2,2,2,1,5,3,2,1,2,2,3,2,2,]
    if message.text == "/start":
      flag = 0
      fr = 0
      keyboard = types.ReplyKeyboardMarkup();
      button_Yes = types.KeyboardButton(text="Да");
      button_No = types.KeyboardButton(text="Нет");
      keyboard.add(button_Yes);
      keyboard.add(button_No);
      bot.send_message(message.chat.id,"Привет, богиня! Ты хочешь позаниматься?",reply_markup=keyboard);
    if message.text == "Да" and flag == 0:
      a = range(10);
      keyboard2 = types.ReplyKeyboardMarkup();
      
      button = types.KeyboardButton(text="Ферменты");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Азотистый обмен");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Липидный обмен");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Витамины");
      keyboard2.add(button);
      
      button = types.KeyboardButton(text="Биологическое окисление");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Углеводный обмен");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Белковый обмен");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Биохимия органов и тканей");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Водно-минеральный обмен");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Биохимия регуляций");
      keyboard2.add(button);

      button = types.KeyboardButton(text="Все сразу");
      keyboard2.add(button);
      
      bot.send_message(message.chat.id,"Выбери тему ",reply_markup=keyboard2);
    
    if message.text == "Нет" and flag == 0:
              keyboard = types.ReplyKeyboardMarkup();
              button_Yes = types.KeyboardButton(text="Да");
              button_No = types.KeyboardButton(text="Нет");
              keyboard.add(button_Yes);
              keyboard.add(button_No);
              bot.send_message(message.chat.id,"О нет :( !!!! Тогда я буду ждать твоего Да...",reply_markup=keyboard);        
   
    if message.text in items:
        keyboard = types.ReplyKeyboardMarkup();
        button_Yes = types.KeyboardButton(text="Начать");
        keyboard.add(button_Yes);
        item = message.text
        bot.send_message(message.chat.id,"Начнем?",reply_markup=keyboard);
    
    if message.text == "Нет" and flag == 1:
            bot.send_message(message.chat.id,"Я буду скучать <3 Когда захочешь вернуться напиши мне /start")

            
    if ((message.text == "Начать") or (message.text == "Да" and flag == 1)):

                fl = 0

                if((item == "Все сразу" or fr == 1) and fl == 0):  
                        item = random.choice(items)
                        fr = 1;
                        
                if(item == "Азотистый обмен" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsa) - 1)
                        for x in questionsa[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)

                if(item == "Липидный обмен" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsl) - 1)
                        for x in questionsl[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                        
                if(item == "Ферменты" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsf) - 1)
                        for x in questionsf[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                        
                if(item == "Витамины" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsv) - 1)
                        for x in questionsv[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                        
                if(item == "Биологическое окисление" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionso) - 1)
                        for x in questionso[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                        
                if(item == "Углеводный обмен" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsu) - 1)
                        for x in questionsu[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                        
                if(item == "Белковый обмен" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsb) - 1)
                        for x in questionsb[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                    
                if(item == "Биохимия органов и тканей" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsor) - 1)
                        for x in questionsor[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                        
                if(item == "Водно-минеральный обмен" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsw) - 1)
                        for x in questionsw[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                        
                if(item == "Биохимия регуляций" and fl == 0):
                        fl = 1;
                  
                        n = random.randint(1,len(questionsr) - 1)
                        for x in questionsr[n]:
                            bot.send_message(message.chat.id, x)
                        keyboard = types.ReplyKeyboardMarkup();
                        button_1 = types.KeyboardButton(text="1");
                        button_2 = types.KeyboardButton(text="2");
                        button_3 = types.KeyboardButton(text="3");
                        button_4 = types.KeyboardButton(text="4");
                        keyboard.add(button_1);
                        keyboard.add(button_2);
                        keyboard.add(button_3);
                        keyboard.add(button_4);
                        bot.send_message(message.chat.id, "Введите ответ", reply_markup=keyboard)
                        

                  
                      
                 
                        
    if item == "Азотистый обмен":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == a[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(a[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);
                                    flag = 1;
    if item == "Ферменты":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == f[ n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(f[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);
                                    flag = 1;

    if item == "Липидный обмен":
                             if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == l[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(l[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);
                                    flag = 1;

    if item == "Витамины":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == v[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(v[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);
                                    flag = 1;

    if item == "Биологическое окисление":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == o[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(o[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);
                                    flag = 1;
                                    
    if item ==  "Углеводный обмен":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == u[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(u[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);
                                    flag = 1;
    if item ==  "Белковый обмен":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == b[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(b[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);
                                    
    if item ==  "Биохимия органов и тканей":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == or_[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(or_[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);
                                    
    if item ==  "Водно-минеральный обмен":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == w[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(w[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);

    if item ==  "Биохимия регуляций":
                                if(message.text == "1" or message.text == "2" or message.text == "3" or message.text == "4"):
                                    print(n)
                                    if(int(message.text) == r[n - 1]):
                                        bot.send_message(message.chat.id,"Ура! Ты потрясающая! Все верно")
                                    else:
                                        bot.send_message(message.chat.id,"Что-то не так, ответ " + str(r[n - 1]))
                                    keyboard = types.ReplyKeyboardMarkup();
                                    button_Yes = types.KeyboardButton(text="Да");
                                    button_No = types.KeyboardButton(text="Нет");
                                    keyboard.add(button_Yes);
                                    keyboard.add(button_No);
                                    bot.send_message(message.chat.id,"Продолжаем?",reply_markup=keyboard);                                         

bot.polling(none_stop=True, interval=0)        
            
