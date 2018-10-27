import random

mylista = random.sample(range(30), 15)
mylistb = random.sample(range(30), 20)
mylistsame = []
print(mylista)
print(mylistb)

for i in mylista:
    if i in mylistb:
        mylistsame.append(i)

print(mylistsame)
