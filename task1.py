def max_getter(developers_struct):
    """
    :param developers_struct: <dict> Структура со всеми разработчиками
    :return: <list> Список игр разработчика с максимальным колличеством игр
    """
    pass


def counter(developers_struct):
    """
    :param developers_struct: Структура со всеми разработчиками
    :return: Два списка: список разрабов, и список колличеств игр каждого из них
    """
    developers_list = []
    counts_list = []
    for dev in developers_struct:
        developers_list.append(dev)
        counts_list.append(len(developers_struct[dev]))
    return developers_list, counts_list


def informator(csv_filename):
    """
    Принимает путь к csv файлу и возвращает нужную структуру
    :param csv_filename: <str> путь к файлу
    :return: <dict> Словарь всех разработчиков.
    (Каждому имени соответствует список со всеми играми-словарями)
    """
    pass


def printer(games):
    """
    Выводит АЙДИ и названия игр от разработчика,
    который выпустил больше всего игр
    :param games: список из словарей-игр одного разработчика
    :return: None
    """
    pass


def painter(developers, counts):
    """
    Строит график
    :param developers: <list> Список всех разработчиков
    :param counts: <list> Список соответствующих количеств игр
    :return: None
    """
    pass


def main():
    """
    Главный менеджер программы.
    Выводит и строит график
    :return: None
    """
    filename = "../steam.csv"

    developers_struct = informator(filename)
    developers_list, counts_list = counter(developers_struct)
    games_of_max_developer = max_getter(developers_struct)
    printer(games_of_max_developer)
    painter(developers_list, counts_list)


if __name__ == "__main__":
    main()
