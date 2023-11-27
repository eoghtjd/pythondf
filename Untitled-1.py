# 1번
q=int(input("몇줄: "))

n="*"
for i in range(1,q):
    print(n*i)

# 2번
q=int(input("몇줄: "))
n="*"
for i in range(1,q):
    print(f'{" "*(q-i)}{n*i}')

# 3번
q=int(input("몇줄: "))
n="*"
for i in range(1,q):
    print(f'{" "*(q-i)}{"*"*(i-1)}{"*"}{"*"*(i-1)}')