import plotly
import plotly.graph_objects as go


def max_getter(developers_struct):
    """
    :param developers_struct: <dict> Структура со всеми разработчиками
    :return: <list> Список игр разработчика с максимальным колличеством игр
    """
    max_count = float('-inf')
    max_dev = ""
    for dev in developers_struct:
        games_count = len(developers_struct[dev])
        if games_count > max_count:
            max_count = games_count
            max_dev = dev

    return developers_struct[max_dev]


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
    appid, name, developer
    """
    with open(csv_filename, encoding='utf-8') as file:
        headers = file.readline().rstrip().split(',')
        indexes_of_headers = {
            "appid": -1,
            "name": -1,
            "developer": -1
        }
        for i in range(len(headers)):
            for header in indexes_of_headers:
                if header == headers[i]:
                    indexes_of_headers[header] = i

        assert all([indexes_of_headers[header] != -1 for header in indexes_of_headers])

        developers_struct = {}
        for line in file:
            game_list = line.rstrip().split(',')
            developer = game_list[indexes_of_headers['developer']]
            game = {
                'id': int(game_list[indexes_of_headers['appid']]),
                'name': game_list[indexes_of_headers['name']]
            }
            if developer in developers_struct:
                developers_struct[developer].append(game)
            else:
                developers_struct[developer] = [game]
    return developers_struct


def printer(games):
    """
    Выводит АЙДИ и названия игр от разработчика,
    который выпустил больше всего игр
    :param games: список из словарей-игр одного разработчика
    :return: None
    """
    for game in games:
        print(f'{game["id"]} - {game["name"]}')


def vijimatel(developers, counts, count=40):
    """
    Выжимает топ 40 разработчиков из соответствующих списков
    :param developers: <list>
    :param counts: <list>
    :return: обрезанные списки
    """
    ogr = len(counts) - 1
    while ogr >= len(counts) - count:
        i = 0
        while i < ogr:
            if counts[i] > counts[i + 1]:
                counts[i], counts[i + 1] = counts[i + 1], counts[i]
                developers[i], developers[i + 1] = developers[i + 1], developers[i]
            i += 1
        ogr -= 1

    return developers[-count:], counts[-count:]


def painter(developers, counts):
    """
    Строит график
    :param developers: <list> Список всех разработчиков
    :param counts: <list> Список соответствующих количеств игр
    :return: None
    """
    developers, counts = vijimatel(developers, counts)
    diagram = go.Pie(labels=developers, values=counts, name="Developers")
    plotly.offline.plot([diagram], filename='developers.html')


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
