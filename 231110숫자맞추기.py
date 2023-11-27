import random

target=random.randint(1,10)
print(target)
while True:
    clinetNumber=int(input("yours? "))
    if target==clinetNumber:
        print('Win')
        break
    else: print('No, try more')