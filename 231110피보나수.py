
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


memory = {1: 1, 2: 1}
count = 0
def fibo_memoization(n):
    global count
    count += 1
    if n in memory:
        number = memory[n]
    else:
       number = fibo_memoization(n-1) + fibo_memoization(n-2)
       memory[n] = number
    return number

# 피보나치 수열의 n번째 항을 계산
n = int(input("n? "))
res = fib(n)
print(f"{n} has {res}입니다.")