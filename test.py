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
        }
    ]
}

developers_list, counts_list = counter(developers_struct)
print(developers_list)
print(counts_list)
