import random
#1
randomList=[]
for i in range(4):
    randomList.append(random.randint(1,100))
    
print(sorted(randomList))