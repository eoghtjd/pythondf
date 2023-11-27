#f=open("./test.txt","w")  #주석처리 Crtl + '/' 누르면 됨
#f.write("hello world\n")  #줄이동   Alt + 방향키 
#f.close()
                            # 전체변수 이름바꾸기 변수누른후 'F2' 누르면 다 바꿀 수 있다.
#f2=open("./test.txt","r")
#print(f2.read())
#f2.close()

#f3=open("./test.txt","a")
#f3.write("Hello world22 \n")
#f3.close()

f2=open("./test.txt","r")
print(f2.read()) #or print(f2.readlines()) <<-한 줄씩 불러온다. print(f2.readlines()) 
f2.close()