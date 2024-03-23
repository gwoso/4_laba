# 7 вариант
## Условие 1 задачи
![image](https://github.com/gwoso/4_laba/assets/150545779/2b531bed-7f95-4a06-80d5-9bfbf3bfb61c)
## Алгоритм
1. __Создаём функцию `decorator`__, которая является декоратором.
2. В это функции создаём обёртку `wrapper`, которая сможет принимать любое количество аргументов.
3. Переменная `result`, в которую записываем принимаемую декоратором функцию
4. Возвращаем результат в диапазоне от 0 до 100
5. Возвращаем `wrapper`
6.  __Создаём функцию `hero`__, перед ней применяя декоратор, отвечающая за героя, инициализируем его текущее `hp = 100`.
7. __Создаём функцию `heal`__, перед ней применяя декоратор, отвечающая за лечение персонажа и принимающая в качестве параметра количество hp, которое будет отхилено.
8. Далее пишется `nonlocal hp` - ключевое слово, которое позволяет присваивать значения переменной во внешней (но не глобальной) области.
9. Хиллим персонажа, не забывая о том, что `hp` должно быть не больше 100.
10. Возвращаем полученное значение `hp`.
11. __Создаём функцию `damage`__, отвечающая за нанесение урона и принимающая в качестве параметра количество hp, которое будет нанесено уроном.
12. Наносим урон персонажу, не забывая о том, что `hp` должно быть не меньше 0.
13. Возвращаем полученное значение `hp`.
14. Возвращаем`heal` и `damage`.
15. Строка `heal, damage = hero()` присваивает возвращаемые функции из замыкания переменным `heal` И `damage`
16. Выводим результат (отнимаем 30 хп и хиллим 40)
## Результат
![image](https://github.com/gwoso/4_laba/assets/150545779/cf015d9c-c972-44dd-8d76-a3a02a898a7b)
## Условие 2 задачи 
![image](https://github.com/gwoso/4_laba/assets/150545779/dcf1cace-4fb7-4391-a48c-44e638d7fbf8)
## Алгоритм
1. Создаём декоратор, а в нём обёртку, которая не будет ничего возвращать.
2. Инициализируем `simple func`, а перед ней используем декоратор
3. Выводим на экран
## Результат
![image](https://github.com/gwoso/4_laba/assets/150545779/7bed03ea-bbca-46ec-9df0-509176055def)
## Источники
1. [](https://www.youtube.com/watch?v=sJF7OMNgLUs)
2. [](https://www.youtube.com/watch?v=v0qZPplzwUQ&t=385s)
3. [](https://stackoverflow.com/questions/3029636/suppressing-a-functions-command-window-output)
