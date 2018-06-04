import re


def readtext(filename):
    # эта функция считывает файл
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


def main():
    # эта функция главная
    sentences = [lst for lst in [(punct(sentence), sentence)
                    for sentence in re.split(r'(\.+|[?!])', readtext("file.txt"))] if len(lst[0]) > 0]
    result_dict = {sentence : {word : len(word) for word in punct_sentence} for punct_sentence, sentence in sentences}
    print('Результат:\n%s' % result_dict)


if __name__ == "__main__":
    main()
