import os
import re



def read_text(filename):
    # эта функция считывает файл
    wfile = open(filename, 'r', encoding='windows-1251')
    text = wfile.read()
    wfile.close()
    return text


def search(word, text):
    match = re.search('<meta content="(.*?)" name="' + word + '"/>', text)
    if match:
        return match.group(1)
    return False


def ans1():
    fw = open("ans1.csv", 'w', encoding="utf-8")
    fw.write("doc_id" + "\t" + "title" + "\t" + "author" + "\t" + "created" + "\t" + "topic" + "\t" + "tagging" + "\n")
    file_list = os.listdir()
    for filename in file_list:
        if filename != 'ex.py':
            text = read_text(filename)
            fw.write(search('docid', text) + "\t" + search('header', text) + "\t" + search('author', text) + "\t" + search('created', text)  + "\t" + search('topic', text) + "\t" + search('tagging', text) + "\n")
    fw.close()


def add_to_dict(word, dictionary):
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1


def ans2():
    dictionary = {}
    regex = '<ana lex="[А-ЯЁ][А-ЯЁ\-]+" gr='
    file_list = os.listdir()
    for filename in file_list:
        if filename != 'ex.py':
            text = read_text(filename)
            res = re.findall(regex, text)
            if res:
                for r in res:
                    match = re.search('ana lex="(.*?)" gr=', r)
                    if match:
                        add_to_dict(match.group(1), dictionary)
    return dictionary


def main():
    # эта функция главная
    ans1()
    #print(ans2())

if __name__ == '__main__':
   main()
