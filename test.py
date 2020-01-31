def printer(games):
    """
    Выводит АЙДИ и названия игр от разработчика,
    который выпустил больше всего игр
    :param games: список из словарей-игр одного разработчика
    :return: None
    """
    for game in games:
        print(f'{game["id"]} - {game["name"]}')


developers_struct = {
    "Valve": [
        {
            "id": 123,
            'name': "Counter - ..."
        },
        {
            "id": 111,
            'name': "Adventure"
        }
    ],
    "Pup": [
        {
            "id": 0,
            'name': "..."
        },
    ]
}

printer(developers_struct["Valve"])
