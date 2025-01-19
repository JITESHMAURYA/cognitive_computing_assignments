import random
import string
for i in range(0,5):
    x=random.randint(1,100)
    print(x,end=" ")
print()

x=random.randint(1,10)
flag = True
print(x)
for i in range(2,x):
    if(x%i==0):
        flag=False
        break
if(flag==False):
    print("not a prime number")
else: 
    print("a prime number")


rolldice=random.randint(1,6)
print(rolldice)

l=[3,2,5,6,35,9,7,19]
item=random.choice(l)
print(item)

random.shuffle(l)
print(l)

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suit = random.choice(suits)
rank = random.choice(ranks)
print(suit,rank)

length=8
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(password)