st = input("Введите слово: ")
for i in range(len(st)):
    print(st)
    st = st[-1:] + st[:-1]
    
