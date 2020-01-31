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


developers = ['lol', 'kek', 'azaza', 'pup', 'geg']
counts = [1, 5, 7, 2, 0]

developers, counts = vijimatel(developers, counts, count=2)
print(developers)
print(counts)
