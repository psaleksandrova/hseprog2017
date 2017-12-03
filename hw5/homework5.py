#4 вариант

st = input("Введите латинское слово: ")
if st == "":
    print("Вы ничего не ввели")
else:
    list = []
    while st != "":
        list.append(st)
        st = input("Введите латинское слово: ")
    with open("inf.txt", "a", encoding="utf-8") as f:
        for i in range(len(list)):
            st = list[i]
            if st[-2:] == "re" or st[-2:] == "ri":
                f.write(st + "\n")
