import databasepublicbank as db

while True:

#def main():
    print ("\n*****  WELCOME TO PUBLIC BANK  *****")
    print ("""
    1.  Open New Bank Account
    2.  Deposit Amount 
    3.  Withdrawal Amount
    4.  Balanc Enquiry
    5.  Display Account Holder's Detail
    6.  Close Bank Account
    7.  Exit 
    """)

    choice = input ("Kindly Select the number to perform the operation (1-7) : ")
    if (choice == '1'):
        db.OpenAc()
    elif (choice == '2'):
        db.DepoAmt()
    elif (choice == '3'):
        db.WithAmt()
    elif (choice == '4'):
        db.BalEnq()
    elif (choice == '5'):
        db.DispAc()
    elif (choice == '6'):
        db.CloseAc()
    elif (choice == '7'):
        print ("\n****** THANK YOU, VISIT AGAIN ******\n")
        break
    else:
        print ("Wrong Input.....")
