def isint(st):
    if len(st) > 1:
        return (st[0].isdigit() or st[0] == '-') and st[1:].isdigit()
    else:
        return st.isdigit()

st = input("Введите температуру в градусах Цельсия: ")
if isint(st):
    a = int(st)
    print("Температура в градусах Фаренгейта:", a * 9 / 5 + 32)
    print("Температура в Кельвинах:", a + 273.15)
