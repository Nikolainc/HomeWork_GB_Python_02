#1) Вводим с клавиатуры целое число X и У.
#Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

#print("Введите число X:")
#numberStart = int(input())
#print("Введите число Y:")
#numberLast = int(input())

#if numberLast < numberStart:
#    numberLast, numberStart = numberStart, numberLast

#counter = 0

#while numberStart <= numberLast:
#    if numberStart % 2 == 0 and numberStart % 3 == 0:
#        counter+=1
#    numberStart+=1

#print(counter)

#==============================================================

#2) Вводим с клавиатуры целое число X
#Далее вводим Х целых чисел.
#Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

#print("Введите кол-во чисел:")
#count = int(input())
#numberFirstMax = 0
#numberSecondMax = 0

#while count > 0:
#    value = int(input())
#    if value > numberSecondMax:
#        numberSecondMax = value
#        if numberSecondMax > numberFirstMax:
#            numberFirstMax, numberSecondMax = numberSecondMax, numberFirstMax
#    count-=1
#print(numberFirstMax)
#print(numberSecondMax)

#==============================================================

#3) Вводим с клавиатуры целое число - это зарплата.
#Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
#И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

#print("Введите зарплату:")
#salary = int(input())

#if (salary / 5000) >= 1:
#   Banknote5000Counter = int(salary / 5000)
#   salary -= 5000 * Banknote5000Counter
#   print(f"Потребуется {Banknote5000Counter} - 5000 банкнот")
#if (salary / 2000) >= 1:
#   Banknote2000Counter = int(salary / 2000)
#   salary -= 2000 * Banknote2000Counter
#   print(f"Потребуется {Banknote2000Counter} - 2000 банкнот")
#if (salary / 1000) >= 1:
#   Banknote1000Counter = int(salary / 1000)
#   salary -= 1000 * Banknote1000Counter
#   print(f"Потребуется {Banknote1000Counter} - 1000 банкнот")
#if (salary / 500) >= 1:
#   Banknote500Counter = int(salary / 500)
#   salary -= 500 * Banknote500Counter
#   print(f"Потребуется {Banknote500Counter} - 500 банкнот")
#if (salary / 200) >= 1:
#   Banknote200Counter = int(salary / 200)
#   salary -= 200 * Banknote200Counter
#   print(f"Потребуется {Banknote200Counter} - 200 банкнот")
#if (salary / 100) >= 1:
#   Banknote100Counter = int(salary / 100)
#   salary -= 100 * Banknote100Counter
#   print(f"Потребуется {Banknote100Counter} - 100 банкнот")
#if (salary / 50) >= 1:
#   Banknote50Counter = int(salary / 50)
#   salary -= 50 * Banknote50Counter
#   print(f"Потребуется {Banknote50Counter} - 50 банкнот")
#if (salary / 10) >= 1:
#   Banknote10Counter = int(salary / 10)
#   salary -= 10 * Banknote10Counter
#   print(f"Потребуется {Banknote10Counter} - 10 банкнот")
#if (salary / 5) >= 1:
#   Banknote5Counter = int(salary / 5)
#   salary -= 5 * Banknote5Counter
#   print(f"Потребуется {Banknote5Counter} - 5 банкнот")
#if (salary / 1) >= 1:
#   Banknote1Counter = int(salary / 1)
#   salary -= 1 * Banknote1Counter
#   print(f"Потребуется {Banknote1Counter} - 1 банкнот")