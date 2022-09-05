import constants #импортируем файл со значением констант

def get_weight(): #заводим инструкцию
   weight = input('Какой твой вес в килограммах? ')
   try: #если вычисления возможно, вернется валидное значение веса
      weight_v = float(weight)
      print("Принято")
      return weight_v
   except: #если валидное значение не вернется, то инструкция запустится вновь
      print("Нужно ввести число")
      get_weight()

def get_growth():
   growth = input('Какой твой рост в метрах? ')
   try: #если вычисления возможно, вернется валидное значение роста
      growth_v = float(growth.replace(',','.'))
      if growth_v > 0:
         print("Принято")
         return growth_v
      else:
         print("Нужно ввести число больше нуля")
         return get_growth()
   except: #если валидное значение не вернется, то инструкция запустится вновь
      print("Нужно ввести число")
      get_growth()




def calc_index(weight, growth, user_name):
   kef = weight / (growth * growth)
   print(user_name + ", твой индекс массы тела " + f'{round(kef, 2)}')  # индекс массы округленный до двух знаков после целого

   if kef >= 40:
      print(constants.FAT_3)

   if 40 > kef >= 35:
      print(constants.FAT_2)

   if 35 > kef >= 30:
      print(constants.FAT_1)

   if 30 > kef >= 25:
      print(constants.FAT_0)

   if 25 > kef >= 18.5:
      print(constants.NORMAL)

   if 18.5 > kef >= 16:
      print(constants.SKINNY)

   if kef < 16:
      print(constants.EX_SKINNY)


def calculate_imt():
   # запрашиваем имя пользователя
   user_name = input("Привет! Как тебя зовут? ")
   # строка приветствия
   print("Рад знакомству, " + user_name + "!")

   weight = get_weight() #значение веса из функции
   growth = get_growth() #значение роста из функции
   calc_index(weight, growth, user_name) #передает значение веса, роста и имя пользователя

calculate_imt()




