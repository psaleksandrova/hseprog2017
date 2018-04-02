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


def search(text):
    # эта функция возвращает первую научную сферу учёного, указанную в карточке
    match = re.search('Научная сфера</th><td>\n(.*?)title="(.*?)"', text)
    if match:
        return match.group(2)
    return False


def write_ans(res):
    with open("ans.txt", "w", encoding="utf-8") as f:
        f.write(res)


def main():
    # эта функция главная
    filename = input('Введите имя файла со статьёй: ')
    while not check_file(filename):
        filename = input('Нет файла с таким названием. Введите заново: ')
    text = read_text(filename)
    res = search(text)
    if not res:
        res = 'Статья не соответсвует нужному формату.'
    write_ans(res)

if __name__ == '__main__':
   main()
