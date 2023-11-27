
f=open("./memberlist.txt","w")
for i in range(3):
    name=input('사용자 이름: ')
    pw=input('사용자 비밀번호: ')
    f.write(name + " " + pw + "\n")


f.close()

f2=open("./memberlist.txt","r")
print(f2.read())  
f2.close()