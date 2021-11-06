class ATM (object):
    def __init__(self,card,pin,amt):
        self.card=card
        self.pin=pin
        self.amt=amt
    def cashwithdrawal(self):
        self.cash=int(input("enter the amount you want to withdraw"))
        num=int(input("enter your pin number"))
        if num == self.pin:
         print("withdrawal transaction successfull !")
        else :  
         print("wrong pin number")  



Niranjana=ATM(7251,1234,10000)
Niranjana.cashwithdrawal()
        