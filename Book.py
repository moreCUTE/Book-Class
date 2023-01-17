import random
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isCheckOut = False
        self.numer = random.randrange(10, 300)
       
    def libro(self):
        print("the book you chenck iout: ", self.title)
        print("authroj of nbok isd: ",self.author)
        print("rasdon nuemre: ",self.numer)
       
    def CheckOut(self):
        if self.isCheckOut == True:
            print("bookj no hewre alreay taken")
        else:
            print("u chec out", self.title)
            self.isCheckOut = True
       
    def CheckIn(self):
        self.isCheckOut = False
       
   
b1 = book("One fish, two fish, red fish, blue fish", "Dr.Seuss")
b2 = book("The Very Hungry Caterpillar", "Eric Carle")
b3 = book("The Rainbow Fish", "Marcus Pfsiter")
b4 = book("No David", "David Shannon ")

b1.libro()
b1.CheckOut()

print("")

b2.libro()
b2.CheckOut()

print("")

b3.libro()
b3.CheckOut()

print("")

b4.libro ()
b4.CheckOut()
