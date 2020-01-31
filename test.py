from json import dumps


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


def print_struct(struct):
    print(dumps(struct, indent=4))


developers_struct = informator("../steam.csv")
print_struct(developers_struct)
