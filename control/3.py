st = input('Введите слово: ')
if st == '':
    print('Вы ничего не ввели')
else:
    list = []
    while st != '':
        list.append(st)
        st = input('Введите слово: ')
a = ['No'] * len(list) #здесь мы будем помечать, встретилось ли заданное слово в словаре

with open("Ozhegov.txt", encoding="utf-8") as f:
    for line in f:
        words = line.split('|')
        for i in range(len(list)):
            if words[0] == list[i]:
                w3 = words[3] #необходимо для того, чтобы убрать перенос строки в конце примера употребления
                list[i] += '-' + w3[:-1] + '-' + words[1]
                a[i] = 'Yes'

for i in range(len(list)):
    if a[i] == 'Yes':
        print(list[i])
    else:
        print('Слово не нашлось')
        
