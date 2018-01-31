# считаем, что формы, образованные от глаголов на -y и -e, заканчиваются на -ied
import re

def readtext(filename):
    # эта функция считывает файл
    filename += '.txt'
    wfile = open(filename, 'r', encoding='utf-8')
    text = wfile.read()
    wfile.close()
    return text


def del_empty(words):
    # эта функция удаляет пустые слова из текста
    while '' in words:
        words.remove('')
    return words


def punct(text):
    # эта функция убирает знаки препинания из текста
    # и удаляет образовавшиеся пустые слова
    words = re.split(r'[\s.,()—:`;"-*&!?\'“”]+', text)
    del_empty(words)
    return words


def check(word):
    # эта функция проверяет, заканчивается ли слово на ed(1) и ied(2)
    # иначе возвращает 0
    if word.endswith('ed'):
        if word.endswith('ied'):
            return 2
        else:
            return 1
    return 0
    

def add_to_dict(word, dictionary):
    # эта функция добавляет слово в словарь, если его там нет
    if word not in dictionary:
        dictionary[word] = True


def count(words):
    # эта функция подсчитывает количество слов на ed и ied во всём тексте
    dict_ed = {}
    dict_ied = {}
    for word in words:
        word = word.lower()
        ch = check(word)
        if ch > 0:
            add_to_dict(word, dict_ed)
        if ch == 2:
            add_to_dict(word, dict_ied)
    return len(dict_ed), len(dict_ied)


def main():
    # эта функция главная
    words = punct(readtext(input('Введите имя файла с текстом: ')))
    c_ed, c_ied = count(words)
    print('В тексте', c_ed, 'форм на -ed, из них', c_ied, 'образованы от глаголов на -y  или -e.')
    

if __name__ == '__main__':
    main()
