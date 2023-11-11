# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил(а):
- Якимов Данила Дмитриевич
- АИС-21-1

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Самостоятельная работа №1
### При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных

### Результат.

![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/1.png)

## Выводы
- 1)Считываем строку ввода.
- 2) Разделяем строку на числа по пробелу и сохраняем в список userInfoList
- 3) Преобрарузем список userInfoList в кортеж userInfoTuple
- 4) Выводим список и кортеж в консоль

## Самостоятельная работа №2
### Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже(в этом случае кортеж вернется функцией в исходном виде). Входные данные: (1, 2, 3), 1) (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3) (2, 4, 6, 6, 4, 2), 9) Ожидаемый результат: (2, 3) (1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2) (2, 4, 6, 6, 4, 2)

### Результат.

![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/2.1.png)
![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/2.2.png)
![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/2.3.png)

## Выводы
- 1) Считываем строку ввода и создаем пустой список strNums
- 2) Проверяем являеется ли символ числом и если да, то добавляем в конец списка strNums
- 3) Запоминаем последнее число в переменную positionToDelete и удаляем его из списка (последнее число - позиция с которой должна быть удалена цифра в списке)
- 4) Проверяем, есть ли в данной позиции число, если есть то удаляем, преобразуем список в кортеж и выводим кортеж, если нет просто преобразуем список в кортеж и выводим.


## Самостоятельная работа №3
### Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количеств этих чисел в имеющейся последовательности. Для построения словаря создайте функцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.

### Результат.

![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/3.png)

## Выводы
- 1) Создаем пустой словарь userNums_dic
- 2) Для каждого числа в строке проверяем есть ли оно в словаре, если нет, то добавляем его как ключ, устанавливаем значение равное кол-ву упоминаний этого числа в строке
- 3) Сортируем словарь по значениям в порядке убывания и удаляем все значения кроме трех первых
- 4) Сортируем по ключам в порядке возрастания
- 5) Выводим в консоль словарь из трех значений (ключ - число,  значение - кол-во упоминаний)

## Самостоятельная работа №4
### Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного. Входные данные: (1, 2, 3), 8) (1, 8, 3, 4, 8, 8, 9, 2), 8) (1, 2, 8, 5, 1, 2, 9), 8) Ожидаемый результат: () (8, 3, 4, 8) (8, 5, 1, 2, 9)

### Результат.

![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/4.1.png)
![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/4.2.png)
![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/4.3.png)

## Выводы
- 1)Считываем строку
- 2)Создаем два пустых списка strIDPass и strIDToCheck.
- 3)Создаем переменную count и устанавливаем ее значением 0.
- 4)Проверяем каждый символ в введенной строке, если число то добавляем в конец списка strIDPass. Если предпоследний символ совпадает с текущим числом, то номер текущей позиции добавляем в список strIDToCheck.
- 5)Удаляем последний элемент из списка strIDPass (Последнее число - ID который надо отыскать в списке).
- 6)Пробуем создать кортеж из элементов strIDPass в диапазоне от элемента [0] списка strIDToCheck до элемента [1] списка strIDToCheck и вывести его
- 7)При возникновении исключения выводим пустой кортеж.

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, в которой будут обязательно использоваться кортеж или список. Проведите минимум три теста для проверки работоспособности вашей задачи.
#### Программа которая принимает на вход последовательнотсь чисел, разделяет их на четные и нечетные. Ответ выводит в виде двух кортежей.
### Результат.

![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/5.1.png)
![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/5.2.png)
![Меню](https://github.com/qwedani/Software_Engineering/blob/Тема-6/pic/5.3.png)

## Выводы
- 1)Принимаем строку от пользователя
- 2)Преобразуем строку в список с разделяющим символом пробела и записываем в список strTuple (не правильно назвал, следовало бы strList)
- 3)Создаем два пустых листа evenList и oddList (для четных и нечетных)
- 4)Проверяем каждое число в списке strTuple, если делится без остатка на 2, то добавляем в список evenList, иначе в список oddList
- 5)Выводим списки evenList и oddList в консоль

