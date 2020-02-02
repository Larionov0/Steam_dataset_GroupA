def super_split(string, sep, bracket='"'):
    ignore = False
    words = []
    start_index = 0
    for i in range(len(string)):
        if string[i] == bracket:
            ignore = not ignore
        elif string[i] == sep and not ignore:
            substring = string[start_index:i]
            words.append(substring)
            start_index = i + 1
    return words


text = "Kek,lol,azaza,\"I, I, I\",100"

print(super_split(text, ","))
