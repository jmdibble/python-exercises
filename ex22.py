with open("names.txt") as open_file:
    line = open_file.readlines()

line = [x.strip() for x in line]

occur = dict((x,line.count(x)) for x in set(line))

print(occur)



