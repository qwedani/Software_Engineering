"""
Программа которая принимает на вход последовательнотсь чисел, разделяет их на четные и нечетные.
Ответ выводит в виде двух кортежей
"""

def evenOdd():
    str = input()
    strTuple = str.split(" ")
    evenList = []
    oddList = []

    for num in strTuple:
        if int(num) % 2 == 0:
            evenList.append(int(num))
        else:
            oddList.append(int(num))
    print(evenList)
    print(oddList)

evenOdd()
