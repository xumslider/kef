user_name = input("Привет! Как тебя зовут? ") #запрашиваем имя пользователя
print("Рад знакомству, " + user_name + "!") #строка приветствия


weight = input ( 'Какой твой вес в килограммах? ') # задаем переменную "Вес" с введенными данными пользователя
weight_v = float(weight)                # переводим введенные данные во float

growth = input ( "Какой у тебя рост в метрах? " ) # задаем переменную "Рост" с введенными данными пользователя
growth_v = float(growth.replace(',', '.')) #переводим введенные данные во float с заменой запятой на точку

kef = weight_v / (growth_v * growth_v) # индекс массы тела = вес деленный на квадрат роста
print(user_name + ", твой индекс массы тела " + f'{round(kef, 2)}') #индекс массы округленный до двух знаков после целого

if kef >= 40:
    print( 'Этот результат соответствует третьей степени ожирения. Тебе срочно нужно обратиться за помощью к специалисту.' )

if 40 > kef >= 35:
    print( 'Этот результат соответствует второй степени ожирения. Тебе нужна помощь специалиста, изменения в стиле питания и образе жизни.')

if 35 > kef >= 30:
    print('Этот результат соответствует первой степени ожирения. Тебе необходимо снизить калорийность рациона и увеличить активность.')

if 30 > kef >= 25:
    print('У тебя избыточная масса тела. Следи за калориями и больше двигайся, чтобы прийти в норму.')

if 25 > kef >= 18.5:
    print('Твой вес в норме. Ты отлично справляешься! Продолжай в том же духе!')

if 18.5 > kef >= 16:
    print('Твой вес ниже нормы. Возможно тебе стоит сбавить активность, увеличить калорийность рациона или пить больше воды.'
          '\nПодробнее о твоем состоянии может рассказать специалист.')

if kef < 16:
    print('У тебя серьезный дефицит массы тела. Тебе срочно нужна помощь специалиста')