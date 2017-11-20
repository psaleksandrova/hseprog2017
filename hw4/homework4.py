all_words = 0
s = 0
with open("text.txt", encoding="utf-8") as f:
    for line in f:
        words = line.split()
        for st in words:
            flag = 0
            for c in st:
                if c.isalpha(): #считаем, что последовательность символов - слово, если хотя бы один из символов - буква (т.е. "аль.пака", к примеру, - одно слово)
                    flag = 1
            if flag == 1:
                all_words += 1
                if st[-1:] != '.' and st[-1:] != ',':
                    s += 1

if all_words == 0:
    print('Вы не ввели никаких слов')
else:
    print(s * 100 / all_words, '%', sep = '')
