# Острова 65
## Сборщик информации с новостных сайтов Сахалина
Программа полностью написана на языке программирования python.
Из-за своей кроссплатформенности его можно портировать куда угодно.
Ядром программы является файл `parser.py`.

## Работа ядра системы

Все ядро работает на парсе данных с сайтов, которые поставляют информацию Сахалинской области.
С помощью библиотеки `BeautifulSoap4`. Мы получаем в массивы данные со страницы новостей. ID в массиве топика и ссылки идентичен.
Вся система **_анархична_** ваши конфигы и т.д не уходят в сеть, а все запросы делаются с помощью ненастоящего пользователя.
Так что вы в полной безопасности. Все ваши данные не уходят дальше вашего устройства. Все предпочтения сделаны на основе просмотров сайтов и вашего личного конфига 
`config.txt`. Весь парс новостей происходит на устройстве пользователя. Также при парсе отсеивается лишний мусор из тег символов в html.


## Работа GUI

Для простоты показания концепта был выбран tkinter из-за простоты самой библиотеки. В самом приложении малый дизайн, но этого достаточно чтобы понять функционал.
Его основная задача дать интерфейс ядру, но программой можно спокойно пользоваться и без GUI, но для этого потребуются доп. настройки.



## Конфиг пользователя

Он работает на простом принципе -> вы выбираете любимые топики, интересующий город, и всё.
