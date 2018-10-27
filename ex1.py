import datetime

name = str(input("Give me your name: "))
age = int(input("Give me your age: "))
year = int(datetime.datetime.today().year)
year100 = int(year + 100 - age)

print(name,", you will turn 100 in ",year100,)
