import re
import os


def read_text(filename):
    # эта функция считывает файл
    wfile = open(filename, 'r', encoding='utf-8')
    text = wfile.read()
    wfile.close()
    return text


def check_file(filename):
    # эта функция проверяет существование файла с заданным именем
    return os.path.exists(filename)


def check(word):
    # эта функция проверяет, является ли слово формой глагола "выпить"
    match = re.search(r'вып(ь(ю((сь)?|т(ся)?)|е((шь|м)(ся)?|т((ся)?|е(сь)?)))|ей((ся)?|те(сь)?)|'
                      r'и(т(ь(ся)?|ы[йе]?|(а(я)?)?|о(е)?)|л((ся)?|[аои](сь)?)|'
                      r'в(ш((ий|ая|ое|ие)(ся)?|и(сь)?))?))\b', word)
    if match:
        return match[0]
    return False


def add_to_dict(word, dictionary):
    # эта функция добавляет слово в словарь, если его там нет
    if word not in dictionary:
        dictionary[word] = True


def search(text):
    # эта функция создаёт словарь с формами "выпить", которые присутсвуют в тексте
    dictionary = {}
    words = text.split()
    for word in words:
        match = check(word)
        if match:
            add_to_dict(match, dictionary)
    return dictionary


def main():
    # эта функция главная
    filename = input('Введите имя файла с текстом: ')
    while not check_file(filename):
        filename = input('Нет файла с таким названием. Введите заново: ')
    text = read_text(filename).lower()
    dictionary = search(text)
    if len(dictionary) == 0:
        print('В этом тексте нет форм глагола "выпить"')
    else:
        print('В этом тексте присутствуют следующие формы глагола "выпить":', end = ' ')
        for word in dictionary:
            print(word, end = ' ')


if __name__ == '__main__':
   main()
