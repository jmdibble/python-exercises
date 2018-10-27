import random

#this does not guarantee a mixture of lower and upper, a number and a symbol. My answer is better.

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 12
p = "".join(random.sample(s, passlen))
print(p)