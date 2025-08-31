# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:

    def __init__(self,TrainNo):
        self.TrainNo = TrainNo

    def Book(self,fro,to):
        print(f"Ticket is booked in tainNo is : {self.TrainNo} from {fro} to {to} ")
        

    def GetStatus(self):
        print(f"TainNo: {self.TrainNo} is running...")

    def GerFare(self,fro,to):
        print(f"Ticket fare in tainNo is : {self.TrainNo} from {fro} to {to} Seat No: {randint(222,555)}")
    

Trainno = randint(1000,77777)

r = Train(Trainno)
r.Book("Delhi","Kolkata")
r.GetStatus()
r.GerFare("Delhi","Kolkata")

