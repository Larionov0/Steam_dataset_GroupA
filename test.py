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


developers_struct = {
    "Valve": [
        {
            "id": "123",
            'name': "Counter - ..."
        },
        {
            "id": "111",
            'name': "Adventure"
        }
    ],
    "Pup": [
        {
            "id": "",
            'name': "..."
        },
    ]
}

print(max_getter(developers_struct))
