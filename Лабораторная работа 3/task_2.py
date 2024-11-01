# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=","):
    # Разделение строк участников на списки
    set1 = set(group1.split(delimiter))
    set2 = set(group2.split(delimiter))

    # Находим общих участников, сортируем и возвращаем
    common_participants = sorted(set1 & set2)
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем, отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники:", result)