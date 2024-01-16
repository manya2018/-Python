# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first,participants_second,delimiter = ","):

    participants_list_1 = participants_first.split(delimiter)
    participants_list_2= participants_second.split(delimiter)
    coincidences = list(set(participants_list_1).intersection(participants_list_2))
    coincidences.sort()
    return coincidences
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,"|"))
