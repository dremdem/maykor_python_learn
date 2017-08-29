import requests #импорт библиотек
from bs4 import BeautifulSoup as BS #импорт библиотек

def load_url(uri): # функция базового урл, параметр может быть пустым
    url = 'https://yandex.ru'+ str(uri) # задаем урл для парсинга и при необходимости добавляем необходимую строку
    return url # возвращаем строку урла
def get_requests(additionally): # функция запроса. В параметре передаем строку части урла исключая домен
    #additionally = '/pogoda/moscow'
    response = requests.get(load_url(additionally)).content # выполняем запрос к переданной строке урла
    request = BS(response, "html.parser") # разбираем ответ как html
    return request # возвращаем результат разбора
def find(request,tag,attr): # функция поиска
    text = request.find_all(tag, attr) # ищем необходимый тэг по заданным атрибутам (класс, якорь и т.п.)
    return text # возвращаем результат

def parse_file_bs(request): # функция парсинга
    try: # проверяем на исключения
        results = [] # создаем пустой список
        li_list = request.find_all('li', {'class': 'i-bem'}) # ищем все теги li с классом i-bem
        for item in li_list: # перебираем все, что нашли
            day_name = item.find('span', {'class': 'forecast-brief__item-day-name'}).text # выбираем день недели (пн, вт и т.д) из тега span с классом forecast-brief__item-day-name
            day = item.find('span', {'class': 'forecast-brief__item-day'}).text # выбираем число месяца из тега span с классом forecast-brief__item-day
            comment = item.find('div', {'class': 'forecast-brief__item-comment'}).text # выбираем коментарии (облачно, дождь и т.д)
            temp_day = item.find('div', {'class': 'forecast-brief__item-temp-day'}).text # выбираем температуру дневную
            temp_night = item.find('div', {'class': 'forecast-brief__item-temp-night'}).text # выбираем температуру ночную

            results.append({ # в список добавляем собранные данные
                    'day_name': day_name,
                    'day': day,
                    'comment': comment,
                    'temp_day': temp_day,
                    'temp_night': temp_night
                })
        return results # возвращаем результат
    except requests.exceptions.ReadTimeout:
        print('Время чтения истекло!')
    except requests.exceptions.ConnectTimeout:
        print('Время подключения истекло!')
def print_all(results): # функция вывода всех результатов
    for i in results: # перебираем в цикле данные из results
        print (i['day_name']+' '+i['day']+' '+i['comment']+', Температура:'+i['temp_day']+','+i['temp_night']+'\n')
def init(): # основная функция
    try:
        requests = get_requests('/pogoda/moscow/choose') # делаем запрос к базовому урл со строкой

        samples = requests.find_all("a", "link place-list__item-name") # выбираем все теги 'a' с классом link place-list__item-name
        n = 1 # указываем счетчик для вывода номера города
        console_url = {} # создаем словарь
        for i in samples: # перебираем все найденные теги в цикле
            print (str(n)+') '+str(i.get_text())) # выводим на экран номер города по порядку из счетчика и текст из найденной ссылки
            console_url[n] = i['href'] # в словарь заносим номер города из счетчика как ключ и ссылку как значение
            n += 1 # увеличиваем счетчик
        print ('\n Введите число нужного города  \n')
        a = int(input()) # присваиваем введенный номер в переменную 'a'
        try:
            print ('Выбранный город: '+samples[a-1].get_text()+' \nНа сколько дней вывести?\n1) на 10 дней \n2) за 1 день')
            requests = get_requests(console_url[a]) # запрашиваем страничку в соответствии с введеным значением. В параметре передаем строку (часть урл с названием города)
            res = parse_file_bs(requests) # парсим результат
        except :
            print('Введите номер из списка!')
        b = int(input()) # создаем еще одну переменную с введенной информацией (первая еще нужна)
        if b == 1: # если ввели 1
            print ('Город: '+samples[a-1].get_text()+'\n') # выводим название введеного города
            print_all(res) # вызываем функцию печати всех результатов
        if b == 2: # если ввели 2
            print ('выберите число\n')
            z = 1 # указываем счетчик для вывода дней
            for i in res: # перебираем результать в цикле
                print (str(z)+') '+i['day']+' ('+i['day_name']+')') # выводим порядковый номер, день и день недели
                z += 1 # увеличиваем счетчик
            b = int(input())# создаем переменную для выбора даты (перетираем предыдущее значение, т.к. оно не нужно)
            # выводим на экран значения в соответсвии с выбранным городом и днем
            print ('Выбранный город: '+samples[a-1].get_text()+'! '+res[b-1]['day_name']+' '+res[b-1]['day']+' '+res[b-1]['comment']+', Температура:'+res[b-1]['temp_day']+','+res[b-1]['temp_night']+'\n')
    except :
        print('Введите номер из списка!')

#requests = get_requests('/pogoda/moscow')
#parse_file_bs(requests)

