consonants = ['B', 'b', 'C', 'c', 'D', 'd', 'F', 'f', 'G', 'g', 'H', 'h', 'J',
              'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q',
              'R', 'r', 'S', 's', 'T', 't', 'V', 'v', 'W', 'w', 'X', 'x', 'Y',
              'y', 'Z', 'z']
st = input('Введите фразу: ')
for i in range(len(st)):
    print(st[i], end = '')
    if st[i] in consonants:
        print('aig', end = '')
