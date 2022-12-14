import codecs
import csv
import os
import sys


def csv_reader(file_name):
    """ Считывает данные из csv файла
    :param file_name: Имя файла с расщирением
    :return: list Список данных
    """
    file = codecs.open(file_name, 'r', 'utf_8_sig')
    reader = csv.reader(file)
    data = list(reader)
    file.close()
    return data


def year(ls):
    """ Извлекает год из списка
    :param ls: Список
    :return: int Год из списка
    >>> Keys.published_at = 2
    >>> year(["This",'is','5'])
    5
    >>> Keys.published_at = 2
    >>> year(["This",'is','12345'])
    1234
    """
    return int(ls[Keys.published_at][0:4])


class ProfKeys:
    """ Класс для хранения индексов нужных строк
    Attributes:
        name (str): Название
        salary_from (int): Мин зп
        salary_to (int): Макс зп
        salary_currency (str): Валюта зп
        area_name (str): Место вакансии
        published_at (str): Дата публикации
    """
    def __init__(self, headers):
        """ Инициализирует класс с данными
        :param headers: Список с заголовками
        >>> type(ProfKeys(['name','salary_from','salary_to','salary_currency','area_name','published_at'])).__name__
        'ProfKeys'
        >>> ProfKeys(['name','salary_from','salary_to','salary_currency','area_name','published_at']).area_name
        4
        >>> ProfKeys(['name','salary_from','salary_to','sos','salary_currency','area_name','published_at']).area_name
        5
        """
        self.name = headers.index('name')
        self.salary_from = headers.index('salary_from')
        self.salary_to = headers.index('salary_to')
        self.salary_currency = headers.index('salary_currency')
        self.area_name = headers.index('area_name')
        self.published_at = headers.index('published_at')


data = csv_reader(input())

head = data.pop(0)

Keys = ProfKeys(head)

years_csv_files = {}

if not os.path.exists("chunks_csv"):
    os.mkdir("chunks_csv")


# Заполняю словарь открытыми файлами и записываю построчно. Вроде как экономит время.
for line in data:
    temp_year = year(line)
    if temp_year not in years_csv_files:
        years_csv_files[temp_year] = codecs.open(f"chunks_csv/{temp_year}.csv", 'w', 'utf_8_sig')
    csv.writer(years_csv_files[temp_year]).writerow(line)

# Прошлый вариант не сработал(
[x.close() for x in years_csv_files.values()]
