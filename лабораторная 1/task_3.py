list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count = len(list_players)
first = list_players[: count//2 ]
second = list_players[count//2 :]
print(first)
print(second)
