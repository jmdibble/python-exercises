import random
l = [random.randrange(30) for i in range(50)]
print(l)

def dupesa(x):
    return(list(set(l)))

def dupesb(x):
    new = []
    for i in x:
        if i not in new:
            new.append(i)
            new.sort()
    return new

print(dupesa(l))
print(dupesb(l))