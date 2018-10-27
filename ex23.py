with open("one.txt") as open_file:
    line_one = open_file.readlines()

line_one = [x.strip() for x in line_one]
# print(line_one)

with open("two.txt") as open_file:
    line_two = open_file.readlines()

line_two = [x.strip() for x in line_two]
# print(line_two)

matches = []

for i in line_one:
    if i in line_two:
        matches.append(i)

print(matches)