class opr:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b==0:
            print('error')
        else:
            return self.a/self.b
        
tt=opr(1,0)
print(tt.sub())
print(tt.mul())
print(tt.add())
print(tt.div())
