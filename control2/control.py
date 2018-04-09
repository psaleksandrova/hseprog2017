import re


def read_text(filename):
    # эта функция считывает файл
    wfile = open(filename, 'r', encoding='utf-8')
    text = wfile.read()
    wfile.close()
    return text


def s_xml(text):
    # эта функция подсчитывает число строк заголовка XML в тексте (задание 1)
    s = 0
    for line in text:
        s += 1
        if '</teiHeader>' in line:
            break
    return s


def add_to_dict(morph, dictionary):
    # эта функция добавляет морфологический разбор слова в словарь, если его там нет,
    # и увеличивает количество его вхождений в ином случае
    if morph in dictionary:
        dictionary[morph] += 1
    else:
        dictionary[morph] = 1


def morph(line):
    # эта функция проверяет, содержится ли в строке морфологический разбор слова и возвращает его, если он там есть
    match = re.search('<w lemma=(?:.*?) type="(.*?)"', line)
    if match:
        return match.group(1)
    return False


def count(text):
    # эта функция подсчитывает количество каждого морфологического разбора в тексте
    dictionary = {}
    for line in text:
        m = morph(line)
        if m:
            add_to_dict(m, dictionary)
    return dictionary


def n_gender(line):
    # эта функция проверяет, содержится ли в строке морфологический разбор слова среднего рода и возвращает словоформу
    match = re.search('<w lemma=(?:.*?) type="(f.h.*?)">(.*?)<', line)
    if match:
        return match.group(2)
    return False


def write_ans(res, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(res)


def main():
    # эта функция главная
    text = read_text('F.xml').split('\n')
    write_ans(str(s_xml(text)), 'ans1.txt') # задание 1
    f = open('ans23.txt', 'w', encoding='utf-8')
    dictionary = count(text)
    for mor in dictionary:
        f.write(mor + ' ' + str(dictionary[mor]) + '\n') # задание 2
    f.close()


if __name__ == '__main__':
   main()
