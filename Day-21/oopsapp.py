class App:
    discount=10
    prod=['Footwear','Smartphones','Handbags','Sneakers','Running Shoes','Headphones']

    @classmethod
    def showproducts(cls):
        for i in cls.prod:
            print(i)

    @classmethod
    def showdiscount(cls):
        print('Discount: ',cls.discount)

    def userinfo(self,username,phoneno):
        self.username=username
        self.phoneno=phoneno
        print(f"Welcome to the e-commerce app {self.username}")

    @staticmethod
    def banner():
        print('10% discount is available')
    
user1=App()
user2=App()

user1.userinfo('Abhiram','9803828481')
user1.banner()
App.banner()

App.showdiscount()
App.showproducts()

user1.showdiscount()
user1.showproducts()
