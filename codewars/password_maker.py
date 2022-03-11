'''
https://www.codewars.com/kata/5637b03c6be7e01d99000046/train/python
'''


def make_password(phrase):
    # Your code here
    words = phrase.split(" ")
    y = []
    for x in words:
        y.append(x[0])
    d = "".join(y)
    d = d.replace("o", "0")
    d = d.replace("O", "0")
    d = d.replace("i", "1")
    d = d.replace("I", "1")
    d = d.replace("s", "5")
    d = d.replace("S", "5")
    return d


def make_password(phrase):
    store = {'i': '1', 'I': '1', 'o': '0', 'O': '0', 's': '5', 'S': '5'}
    return ''.join(store.get(a[0], a[0]) for a in phrase.split())
