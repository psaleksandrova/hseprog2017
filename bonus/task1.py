def isint(st):
    if len(st) > 1:
        return (st[0].isdigit() or st[0] == '-') and st[1:].isdigit()
    else:
        return st.isdigit()

st = input('Введите число: ')
if not isint(st):
    if st == '':
        print('Вы совсем ничего не ввели')
    else:
        print('Вы ввели не число')
if isint(st):
    s = int(st)
    n = 1
    mn = s
    mx = s
    st = input('Введите число: ') 
    while st != '':
        if isint(st):
            a = int(st)
            s += a
            n += 1
            mn = min(mn, a)
            mx = max(mx, a)
        else:
            print('Вы ввели не число')
        st = input('Введите число: ')
        
    print('Среднее арифметическое:', s / n)
    print('Минимальное число:', mn)
    print('Максимальное число:', mx)

