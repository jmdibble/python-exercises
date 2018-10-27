import random, string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
number = list(range(0, 9))
symbol = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "/", "~", "`", "[", "]", "{", "}", ":", ";", "@", "<", ">", "?"]

phrase = []

l = random.sample(lower, 3)
u = random.sample(upper, 2)
n = random.sample(number, 2)
s = random.sample(symbol, 2)
n2 = [str(x) for x in n]

l1 = "".join(l)
u1 = "".join(u)
n1 = "".join(n2)
s1 = "".join(s)

phrase.append(l1)
phrase.append(u1)
phrase.append(n1)
phrase.append(s1)

passcode = "".join(phrase)
print("Your random passcode is", passcode)