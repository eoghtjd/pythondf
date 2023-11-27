print("숫자입력하기, 중지-> '중지'")
a=[]

while True:
    n=input("숫자 입력: ")
    if n=="중지":
     break
    a.append(int(n))

print(a)
print("max, min: ", max(a), min(a))


a.remove(max(a))
a.remove(min(a))
print(sum(a)/len(a))