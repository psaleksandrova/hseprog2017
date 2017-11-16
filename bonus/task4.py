vowels = ['А', 'а', 'Е', 'е', 'Ё', 'ё', 'И', 'и', 'О', 'о', 'У', 'у', 'Ы', 'ы',
          'Э', 'э', 'Ю', 'ю', 'Я', 'я']
st = input('Введите слово или фразу: ')
for i in range(len(st)):
    print(st[i], end = '')
    if st[i] in vowels:
        print('с', end = '')
        print(st[i], end = '')
