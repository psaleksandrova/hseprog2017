def property_1(a, b, c):
    if (a + b == c):
        print("Введённые числа обладают свойством 1")
    else:
        print("Введённые числа не обладают свойством 1")

def property_5(a, b, c):
    if (a / b == c):
        print("Введённые числа обладают свойством 5")
    else:
        print("Введённые числа не обладают свойством 5")


a, b, c = map(int, input().split())

property_1(a, b, c)
property_5(a, b, c)
