consonants = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
vowels = 'AaEeIiOoUu'

def capital(c):
    if ord('A') <= ord(c) <= ord('Z'):
        return chr(ord(c) + ord('a') - ord('A'))
    else:
        return c

text = input()
words = text.split()
for st in words:
    if st.isalpha():
        if st[0] in consonants:
            st = st[1:] + capital(st[0])
            while st[0] in consonants:
                st = st[1:] + st[0]
            st = st + 'ay'
        elif st[0]:
            st = st + 'way'
    print(st, end = ' ')
