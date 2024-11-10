# Функция для поиска общих участников
def find_common_participants(group1, group2, delimiter=","):
    # Создаем множество только для первой группы
    set_group1 = set(group1.split(delimiter))

    # Находим пересечения с помощью списка, проверяя участников второй группы
    common_participants = sorted([participant for participant in group2.split(delimiter) if participant in set_group1])

    return common_participants


# Пример использования функции
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции с разделителем, отличным от запятой
result = find_common_participants(participants_first_group, participants_second_group, delimiter="|")
print("Общие участники:", result)
