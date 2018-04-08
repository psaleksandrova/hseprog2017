import re


def read_text(filename):
    # эта функция считывает файл
    wfile = open(filename, 'r', encoding='utf-8')
    text = wfile.read()
    wfile.close()
    return text


def substitution(line):
    # эта функция заменяет все формы слова "философия" на формы слова "астрология"
    result = re.sub(r'([^А-Яа-я])философи((?:я(?:м(?:и)?|х)?|и|ю|(?:е)?й|)[^А-Яа-я])', r'\1астрологи\2', line)
    result = re.sub(r'([^А-Яа-я])Философи((?:я(?:м(?:и)?|х)?|и|ю|(?:е)?й|)[^А-Яа-я])', r'\1Астрологи\2', result)
    return result


def main():
    # эта функция главная
    f = open('ans.txt', 'w', encoding='utf-8')
    text = read_text('Философия.html').split('\n')
    for line in text:
        f.write(substitution(line + '\n'))
    f.close()

if __name__ == '__main__':
   main()
