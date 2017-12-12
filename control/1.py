with open("Ozhegov.txt", encoding="utf-8") as f:
    for line in f:
        words = line.split('|')
        if len(words[0]) >= 20:
            print(line, end = '')
