import os

def add_to_dict(letter, dictionary):
    # эта функция добавляет букву в словарь, если её там нет, в ином случае увеличивает частотность
    if letter not in dictionary:
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1


def count():
    # эта функция создаёт словарь с частотностью каждой буквы
    dictionary = {}
    for root, dirs, files in os.walk('.'):
        for dirname in dirs:
            add_to_dict(dirname[0].lower(), dictionary)
    return dictionary


def main():
    # эта функция главная
    dictionary = count()
    if dictionary:
        mx = max(dictionary.values())
        # для того, чтобы получить ключ по значению, создаём инверсию словаря
        inv_dict = {value: key for key, value in dictionary.items()}
        print('Большинство папок начинается на букву', inv_dict[mx])


if __name__ == '__main__':
    main()
