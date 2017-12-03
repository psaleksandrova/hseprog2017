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
            if st[-3:] == "are" or st[-3:] == "ere" or st[-3:] == "ire" or st[-3:] == "ari" or st[-3:] == "eri" or st[-3:] == "iri":
                f.write(st + "\n")
