consonants = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
st = input('Введите фразу: ')
for i in range(len(st)):
    print(st[i], end = '')
    if st[i] in consonants:
        print('aig', end = '')
