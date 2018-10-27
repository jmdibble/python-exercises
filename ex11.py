## A number is prime if it cannot be divided by anything except itself and 1.

n = int(input("Pick any number: "))
print("Your chosen number was",n)

l = range(2, n)

def is_prime(number):
    for i in l:
        div = number%i
        if div==0:
            return False
        else:
            return True
answer = is_prime(n)
if answer is False:
    print("Not prime :(")
else:
    print("Is prime! :)")