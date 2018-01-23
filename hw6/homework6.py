import random

def syll(a, b):
    # эта функция выбирает случайное количество слогов слова в заданном диапазоне, который и является аргументами функции
    syll = random.randint(a, b)
    return syll

def getword(filename, syll):
    # эта функция считывает случайное слово, опираясь на количество слогов в нужном слове
    # для удобства слова каждой части речи хранятся в отдельных файлах и отсортированы так,
    # что слово с n слогами находится в (n - 1)-ой строке (т.к. нумерация идёт с 0)
    filename += '.txt'
    wfile = open(filename, 'r', encoding='utf-8')
    words = wfile.read().split('\n')
    w = random.choice(words[syll - 1].split())
    wfile.close()
    return w

def gender(noun):
    # эта функция возвращает род существительного, исходя из его последней буквы
    # для упрощения задачи в список слов не попали существительные, имеющие окончание, отличное от a и o
    if noun[-1:] == 'a':
        return 'f'
    return 'm'

def article(noun):
    if gender(noun) == 'f':
        return 'la'
    return 'il'

def noun(noun_s):
    # эта функция выбирает случайное существительное с нужным количеством слогов
    # и возвращает его с артиклем
    noun = getword('nouns', noun_s)
    noun = article(noun) + ' ' + noun
    return noun

def verb(verb_s):
    # эта функция возвращает случайный глагол с нужным количеством слогов
    verb = " " + getword('verbs', verb_s)
    return verb

def adverb(s, noun_s, verb_s):
    # эта функция возвращает случайное наречие с тем количеством слогов, которое осталось свободным в строке
    # если места для наречия не осталось, то функция, соответственно, ничего не возвращает
    if s - 1 - noun_s - verb_s > 0:
        adverb = ' ' + getword('adverbs', s - 1 - noun_s - verb_s)
        return adverb
    return ''

def adj_ending(noun, adjective):
    # эта функция меняет окончание прилагательного, если существительное относится к женскому роду,
    # так как в файле хранятся прилагательные в форме мужского рода
    if adjective == '':
        return adjective
    if gender(noun) == 'f':
        adjective = adjective[:-1] + 'a'
    return adjective

def adjective(s, noun_s):
    # эта функция возвращает случайное прилагательное с тем количеством слогов, которое осталось свободным в строке
    # если места для прилагательного не осталось, то функция, соответственно, ничего не возвращает
    if s - 2 - noun_s > 0:
        adjective = ' ' + getword('adjectives', s - 2 - noun_s)
        return adjective
    return ''

def punct():
    # эта функция возвращает случайный знак препинания
    marks = ['.', '?', '!', '...']
    return random.choice(marks)

def verse1(s):
    # эта функция собирает строку из сущестивтельного с артиклем, глагола и наречия в том случае, если для него остаётся место
    # аргументом функции будет необходимое количество слогов в данной строке
    if s == 5:
        noun_s = syll(2, 3)
    else:
        noun_s = syll(2, 4)
    verb_s = syll(1, min(s - noun_s - 1, 3))
    return noun(noun_s) + verb(verb_s) + adverb(s, noun_s, verb_s) + punct()

def verse2(s):
    # эта функция собирает строку из существительного с артиклем, глагола быть в форме 3л.ед.ч. и прилагательного, если для него остаётся место
    # аргументом функции будет необходимое количество слогов в данной строке
    if s == 5:
        # так как в списке нет прилагательных из 1 слога
        noun_s = 3
    else:
        noun_s = syll(2, 3)
    n = noun(noun_s)
    return 'è ' + n + adj_ending(n, adjective(s, noun_s)) + punct()

def make_verse(s):
    # эта функция выбирает случайный номер из 1,2 и возвращает соответствующую строчку
    verse = random.choice([1,2])
    if verse == 1:
        return verse1(s)
    else:
        return verse2(s)


def main():
    # основная функция, которая собирает все строки и распечатывает хайку
    print(make_verse(5))
    print(make_verse(7))
    print(make_verse(5))

main()

    




