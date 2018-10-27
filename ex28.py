def large(x, y, z):
    seq = [x,y,z]
    seq.sort()
    print(seq[2])
    return seq[2]


a = int(input("Type your first number: "))
b = int(input("Type your second number: "))
c = int(input("Type your third number: "))
large(a, b, c)
