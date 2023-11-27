class Supermarket:
    count=0
    def __init__(self,location,name,product,customer):
        self.location=location
        self.name=name
        self.product=product
        self.customer=customer
        Supermarket.count+=1
    def print_location(self):
        print(self.location)
    def change_category(self,newCatergory):
       
        self.product=newCatergory
        print('Applied')
    def show_list(self):
        print(self.product)
    def enter_customer(self):
        self.count+=1
    def show_info(self):
         print(self.location, self.name,  self.product, self.customer)
    def show_supermarket_count(self):
        print(Supermarket.count)
a=Supermarket('home','iam','tape',1)
a.print_location()
a.change_category('iron')
a.show_info()
a.show_list()
a.enter_customer()
a.show_supermarket_count()

b=Supermarket('aa','bb','cc',2)
b.print_location()
b.change_category('dd')
b.show_info()
b.show_list()
b.enter_customer()
b.show_supermarket_count()