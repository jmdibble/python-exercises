number = int(input("Type any number: "))

lis = range(1, number)

for i in lis:
    div = number%i
    if div==0:
        print(i)
