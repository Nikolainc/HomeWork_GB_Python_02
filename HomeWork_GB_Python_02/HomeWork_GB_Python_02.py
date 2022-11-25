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