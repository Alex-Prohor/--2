# Функция для поиска индекса первого вхождения элемента в списке
def find_item_index(items_list, item):
    # Перебираем список с использованием enumerate для получения индекса и значения
    for i, current_item in enumerate(items_list):
        # Если текущий элемент равен искомому
        if current_item == item:
            return i  # Возвращаем индекс
    return None  # Если элемент не найден, возвращаем None

# Пример использования функции
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции для получения индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
