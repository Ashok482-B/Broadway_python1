import random

#using randint
a=random.randint(1,3)
print(a)

print("================")
#using random()
a=random.random()
print(a)

print("===========")
#using randrange
a=random.randrange(1,3)
print(a)

print("========")
#using choice
a=["red","green","black","pink","white"]
print(random.choice(a))


#shuffle
print("======================")


cards=["J","K","A","Q"]
random.shuffle(cards)
print(cards)
