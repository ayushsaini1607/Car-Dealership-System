#car dealership system

class Car():
    counter=0
    def __init__(self):
        self.model=input("Enter model: ")
        self.color=input("Enter color: ")
        self.time=int(input("Enter how many years of car manufacture: "))
        self.passengers=int(input("Enter no of passengers: "))
        self.price=int(input("Enter the price of the car: "))
        self.mileage=int(input("Enter mileage of the car: "))
        self.reg_no=input("Enter registration no: ")
        self.top_speed=int(input("Enter the top speed of the car: "))
        self.eng=float(input("Enter engine capacity: "))
        self.sale_status=input("Enter sale status of the car,(Y for available, N for sold): ")
        if(self.sale_status=='Y' or self.sale_status=='y'):
            self.sale_status="Available"
        else:
            self.sale_status="Sold"
        Car.counter+=1
    
    def show_all(self):
        print("\nDetails of requested Car:\n")
        print("Registartion No: ",self.reg_no)
        print("Model: ",self.model)
        print("Color: ",self.color)
        print("Years since car manufacture: ",self.time)
        print("No of passengers: ",self.passengers)
        print("Price: ",self.price)
        print("Mileage: ",self.mileage)
        print("Top speed: ",self.top_speed)
        print("Engine capacity: ",self.eng)
        print("Sale status: ",self.sale_status)

    def show_sale_status(self):
        return self.sale_status
    def show_model(self):
        return self.model

    def show_price(self):
        return self.price

    def change_sale_status(self):
        if self.sale_status=="Available":
            self.sale_status="Purchased"
        elif self.sale_status=="Purchased":
            self.sale_status="Available"  
    
    def Total_cars(self):
        return Car.counter

car_list=list()
while True:    
    ch=input("You'll now be prompted to enter the car details...Continue(Y/N)?")
    if ch=='Y' or ch=='y':
        car_list.append(Car())
    elif ch=='N' or ch=='n':
        print("You chose to exit...")
        break
    else:
        ch=input("Invalid Input! Please enter again!")

def purchase_system():

  print("Now displaying the list of models of car...")
  i=1
  for x in car_list:
    print(i,". ",x.show_model())
    i+=1


  while True:
   n=int(input("Enter the serial no. against model to look up for all the details: "))
   if n>Car.Total_cars(car_list[-1]):
       print("Invalid Input!")
   elif n<=0:
       print("Invalid Input!")
   else:
       car_list[n-1].show_all()
   ch=input("You want to look for more cars?(Y/N)")
   if ch=='Y' or ch=='y':
       continue
   elif ch=='n' or ch=='N':
       break
   else:
       print("Invalid Input")
       print("Exiting the purchase system")
   
  ch=input("Do you want to buy the car?(Y/N) ")
  if ch=='Y' or ch=='y':
    if car_list[n-1].show_sale_status()=="Available":
      print("Amount paid: Rs ",car_list[n-1].show_price()," Purchase Successful!")
      car_list[n-1].change_sale_status()
      print("You have purchased the following Car:\n")
      car_list[n-1].show_all()
    else:
      print("The Car has already been purchased!")
      print("Exiting purchase system...")

  else:
     print("You cancelled the purchase!")
     print("Exiting the purchase system...")

def sale_system():
   car_list.append(Car())
   ch=input("Are you sure you want to sell the car?(Y/N)")
   if ch=='Y' or ch=='y':
       print("Amount received: ",car_list[-1].show_price())
       print("Sale Successful")
       print("You sold the follwing Car: \n")
       car_list[-1].show_all()
       print("Exiting the sale system...")
   elif ch=='N' or ch=='n':
       del car_list[-1]
       print("Sale cancelled!")
       print("Exiting the sale system...")
   else:
        print("Invalid Input!")
        print("Exiting the sale system...")

while True:
    print("1. Purchase a car\n2.Sell a car\n3.Exit")
    sys=int(input("Proceed by entering the choice:"))
    if sys==1:
       purchase_system()
    elif sys==2:
       sale_system()
    elif sys==3:
        print("Exiting the Car Dealership System!")
        exit()
    else:
       print("Invalid Choice!")
       print("Exiting...")
       exit()
     
    

    




      
