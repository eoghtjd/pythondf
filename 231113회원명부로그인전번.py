name = input('사용자 이름: ')
pw = input('사용자 비밀번호: ')

f2 = open("./memberlist.txt", "r")
context = f2.readlines()
f2.close()

if name + " " + pw + "\n" in context:
    print("로그인 성공")
    contact = input('연락처: ')

    
    with open("./member_tel.txt", "r") as f3:
        teltxt = f3.readlines()
        print(teltxt)

    found = False
    for i, line in enumerate(teltxt): #enumerate
        if name in line:
            found = True
            teltxt[i] = name + " " + contact + "\n"
            f3.close()
            break

    if not found:
        teltxt.append(name + " " + contact + "\n")

    with open("./member_tel.txt", "w") as f3:
        f3.writelines(teltxt)
        f3.close()

else:
    print("로그인 실패")

print(context)