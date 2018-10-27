sentence = input("Type a random sentence and I will return it in backwards order: ")

def swap(l):
    lis = l.split()
    ord = []
    for i in lis:
        ord.insert(0, i)
    return " ".join(ord)


print(swap(sentence))




