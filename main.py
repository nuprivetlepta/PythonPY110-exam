from conf import MODEL
from faker import Faker
import random
import json

TITLES = "books.txt"
OUTPUT_FILE = "output.json"


def title() -> list[str]:
    """
    Итерирует построчно файл, сепаратором служит перенос строки.
    Полученные строки складывает в список. Из списка случайным индексом
    Получаем названия.
    :return: list[str]
    """
    with open(TITLES, 'r') as f:
        lst_ = []
        for line in f:
            line_list = line.split('\n')
            lst_.append(line_list)
        return lst_[random.randint(1, 15)]



def counter(pk=1) -> int:
    """
    Функция-генератор, начиная со стартового значения увеличивает его на единицу
    при каждом своём вызове. Пока что заглушена. Условной реализацией можно считать
    функцию def.main(), в которой итератор присваивает номера словарям(книгам),
    для чистоты можно задать границы этого диапазона через kwargs, альтернатива.
    :param pk:
    :return: порядковое число итерации
    """
    int_ = pk
    # count = pk
    # while True:
    # count += 1
    #     yield count
    return int_


def year() -> int:
    """
    Случайный генератор года книги в заданных мною рамках
    :return: целое число в диапазоне 1801-2022
    """
    god = random.randint(1801, 2022)
    return god


def page() -> int:
    """
    Генератор количества страниц в заданных рамках,
    можно перенести аргументы для randint как args,
    дав пользователю возможность выбирать диапазон
    :return: целое число, количество страниц.
    """
    page_ = random.randint(20, 999)
    return page_


def book_num() -> str:
    """
    Книжный номер генерируем вызовом Faker из модуля faker
    :return: возвращает в виде строки книжный номер.
    """
    num = Faker('ru_RU').isbn13()
    return num


def rating() -> float:
    """
    Получаем случайный рейтинг по пятибальной системе,
    методом round округляем до четырех знаков после запятой.
    :return: рейтинг в формате float.
    """
    mark = round(random.uniform(1.0, 5.0), 4)
    return mark


def price() -> float:
    """
    Получаем случайную стоимость в заданных рамках,
    округляем до используемых в платежах сотых единиц.
    :return: цена в формате float.
    """
    bucks = round(random.uniform(0.99, 199.99), 2)
    return bucks


def author() -> list:
    """
    Генератор списка возвращает список авторов,
    количество задается случайным числом из модуля
    random в рамках задания.
    :return: список авторов.
    """
    nums = random.randint(1, 3)
    writers = [Faker('ru_RU').name() for _ in range(nums)]
    return writers


def fields() -> dict:
    """
    Функция собирает список из основных данных о книге,
    создаётся словарь.
    :return: словарь с данными о книге.
    """
    dict_ = {"title": title(), "year": year(), "pages": page(), "isbn13": book_num(),
             "rating": rating(), "price": price(), "author": author()}
    return dict_


def main() -> dict:
    """
    Складываем в новый словарь порядковый номер книги,
    далее добавляем данные о книгах.
    :return:  словарь, содержащий в себе еще один словарь.
    """
    wr_dict = {}
    for i in range(0, 100):
        models = MODEL
        pks = counter()
        dict_ = fields()
        wr_dict[i] = {"model": models, "pk": pks, "fields": dict_}
    return wr_dict


if __name__ == '__main__':

    with open(OUTPUT_FILE, 'w', encoding='utf8') as f:
        json.dump(main(), f, indent=4, ensure_ascii=False)
