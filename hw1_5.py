# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
# работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
plus = int(input("Введите выручку: "))
minus = int(input("Введите издержку: "))
if plus == minus:
    print("Фирма работает в 0")
elif plus < minus:
    print("Фирма работает в убыток. Потери:", plus - minus)
else:
    p = plus - minus
    print("Фирма приносит прибыль:", p)
    print("Рентабельность выручки:", p / plus)
    worker = int(input("Введите численность сотрудников фирмы: "))
    print("прибыль фирмы в расчете на одного сотрудника:", "%.2f" % (p / worker))
