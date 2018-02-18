def readtext(filename):
    # эта функция считывает файл
    wfile = open(filename, 'r', encoding='utf-8')
    text = wfile.read()
    wfile.close()
    return text


def add_to_dict(dictionary):
    # эта функция добавляет слово в словарь
    with open('words.csv', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            words = line.split(',')
            word = words[0]
            dictionary[word] = words[1:]


def points(word):
    # эта функция возвращает строку, состоящую из len(word) точек
    st = ''
    for i in range(len(word)):
        st += '.'
    return st


def check(word, answer):
    # эта функция сравнивает правильный ответ и слово пользователя
    # False возвращается в том случае, когда пользователь не отгадывает слово, но хочет попробовать угадать его ещё раз, воспользовавшись другой подсказкой
    if word == answer:
        print('Вы угадали!')
        return True
    print('Вы не угадали...')
    ans = input('Хотите попробовать ещё раз? Ответьте "да" или "нет": ')
    if ans == 'да':
        return False
    return True


def game(dictionary):
    # эта функция отвечает за саму игру
    for word in dictionary:
        print('Попробуйте угадать существительное:')
        clues = list(dictionary[word])
        Flag = False
        now = 0
        while not Flag:
            print(clues[now], points(clues[now]))
            answer = input('Введите ответ: ')
            Flag = check(word, answer)
            if not Flag:
                if now != len(clues) - 1:
                    now += 1
                else:
                    now = 0
        
            
def main():
    # эта функция главная
    dictionary = {}
    add_to_dict(dictionary)
    game(dictionary)
    print('Спасибо за игру!')


if __name__ == '__main__':
    main()
