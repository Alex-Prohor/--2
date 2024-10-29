money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Счетчик месяцев

while money_capital + salary >= spend:
    money_capital += salary - spend  # Обновляем подушку безопасности
    spend *= (1 + increase)  # Увеличиваем траты на 5%
    months += 1  # Увеличиваем счетчик

print("Количество месяцев, которое можно протянуть без долгов:", months)