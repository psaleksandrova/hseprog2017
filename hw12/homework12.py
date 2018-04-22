import os
import re


def name(filename):
    # эта функция возвращает именно название файла, без расширения
    match = re.search('(.+)\.', filename)
    filename = match.group(1)
    return filename


def count():
    # эта функция подсчитывает количество файлов, название которых состоит только из латинских символов
    c = 0
    file_list = os.listdir()
    for filename in file_list:
        if os.path.isfile(filename):
            filename = name(filename)
            if not re.search('[^A-Za-z]', filename):
                c += 1
    return c


def all_names():
    # эта функция выводит название всех функций или папок
    file_list = os.listdir()
    for filename in file_list:
        print(filename, end = '\n')


def main():
    # эта функция главная
    print('Количество файлов, название которых состоит только из латинских символов, равно', count())
    all_names()


if __name__ == '__main__':
   main()
