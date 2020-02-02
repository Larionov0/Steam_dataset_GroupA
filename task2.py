import plotly
import plotly.graph_objs as go


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


def informator(filename, list_of_games):
    """
    :param filename: <str>
    :param list_of_games: <list> Список названий интересующих игр
    :return: <list>  Структура с информацией про все интересующие нас игры
    """
    with open(filename, encoding='utf-8') as file:
        headers = file.readline().rstrip().split(',')
        indexes_of_headers = {
            "name": -1,
            "platforms": -1,
            "positive_ratings": -1,
            "average_playtime": -1,
            "owners": -1
        }
        for i in range(len(headers)):
            for header in indexes_of_headers:
                if header == headers[i]:
                    indexes_of_headers[header] = i

        assert all([indexes_of_headers[header] != -1 for header in indexes_of_headers])

        games_struct = []
        for line in file:
            game_list = super_split(line.rstrip(), ",")
            name = game_list[indexes_of_headers['name']]
            if name in list_of_games:
                game = {}
                game['name'] = name
                platforms = game_list[indexes_of_headers['platforms']].split(";")
                game['count of platforms'] = len(platforms)
                print(name)
                game['positive ratings'] = int(game_list[indexes_of_headers['positive_ratings']])
                game['average playtime'] = int(game_list[indexes_of_headers['average_playtime']])
                game['owners'] = int(game_list[indexes_of_headers['owners']].split('-')[1])
                games_struct.append(game)

        return games_struct


def diag_builder(games_struct, critery):
    """

    :param games_struct: <list>
    :param critery: <str> Критерий, по которому строим диаграму и сравниваем
    :return: <Bar> диаграму
    """
    x, y = [], []
    for game in games_struct:
        name = game['name']
        value = game[critery]
        x.append(name)
        y.append(value)
    diag = go.Bar(x=x, y=y, name=critery)
    return diag


def builder(list_of_games, filename):
    """
    Основная ф-я для построения графика
    :param list_of_games: <list>
    :return: None
    """
    criteries = ["count of platforms", "positive ratings", "average playtime", "owners"]
    games_struct = informator(filename, list_of_games)
    figure = plotly.subplots.make_subplots(rows=2, cols=2)
    i = 0
    for critery in criteries:
        row = i % 2 + 1
        col = i // 2 + 1
        diagram = diag_builder(games_struct, critery)
        figure.append_trace(diagram, row, col)
        i += 1

    plotly.offline.plot(figure, filename="criteries.html")


builder(["Team Fortress Classic", "Peggle Deluxe", "Dimensional Intersection", "Commandos: Behind Enemy Lines", "Hitman: Codename 47", "Dota 2"], "../steam.csv")
