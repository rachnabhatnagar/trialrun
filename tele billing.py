# -*- coding: cp1252 -*-
import os
import pickle
class consumer:
    def __init__(self):
        tel_no=0
        con_no=0
        name=” “
        add=” “
        city= “ “
        op_rdg=0
        cl_rdg=0
        met_call=0s
        free_calls=0
        ge_calls=0
        met_ge=0
        rent=0
        debits=0
        tax=0
        self. credits=0
        self. gross_amt=0
        self. surge=0
        self. net_amt_bef=0
        net_amt_aft=0

    def get_data(self):
        print(,"ENTER THE RECORD:-")
        self.tel_no=int(raw_input("TELEPHONE NO.    :"))
        self.name=raw_input(“NAME             :")
        self.add=raw_input("ADDRESS          :")
        self.city=raw_input( "CITY             :")
        self.op_rdg=raw_input( "OPENING READING  :")
        self.cl_rdg=raw_input( "CLOSING READING  :")
        self. met_calls=self.cl_rdg-self.op_rdg
        self.free_calls=150
        self.rent=360
        if(self.met_calls<self.free_calls ):
            ge_calls=0
            met_ge=0
        else:

            Self.ge_calls=self.met_calls-self.free_calls
            Self.met_ge=self.ge_calls*(.80)

        self.debits=int(raw_input( "DEBITS           :"))
        self.tax=(self.rent+self.met_ge+self.debits)/20
        self. self. gross_amt=(self.met_ge+self.rent+self.tax+self.debits)
        self.credts=int(raw_input( " SELF. CREDITS          :"))
        if( self. credits> self. gross_amt):
            self. net_amt_bef=0
        else:
            self. net_amt_bef= self. gross_amt- self. credits
        if( self. credits>= self. gross_amt)
            self. surge=0
        else:
            self. surge=20
        net_amt_aft=net_amt_bef+ self. surge

    def  show_data(self):
        print("TELEPHONE NO."),self.tel_no
        print("CONSUMER NO."),self.con_no
        print("OPENING READING  "),self.op_rdg
        print(CLOSING READING  ") self.cl.rdg
        print(,"METERED CALLS    ")self.met_call
        print("FREE CALLS       ") self.free-calls
        print(,"GABLE CALLS  "),self.ge_calls
        print("DEBITS          ") self.debits

        print("TAXES           ") self.tax
        print("GROSS AMOUNT    ") self.gross_amt
        print(" SELF. CREDITS         ") self.credits
        print("RENTAL                             ") self.rent
        print("AMOUNT PAYABLE IF PAID ON OR BEFORE ") self.net_amt_bef
        print(" SELF. SURGE                           ") self.surge
        print("AMOUNT PAYABLE IF PAID ON OR AFTER  ") self.net_amt_aft
def search(self,tno):
         
        try:
            print"reading"
            file=open("TELE.DAT","rb")
            count=0
            while  True:
              x=pickle.load(file)
                if(x.ecode==tno):
                    print"record Found!"
                    print("TELEPHONE NO."),x.tel_no
                    print("CONSUMER NO."),x.con_no
                    print("OPENING READING  "),x.op_rdg
                    print("CLOSING READING  ") ,x.cl.rdg
                    print(,"METERED CALLS    "),x.met_call
                    print("FREE CALLS       ") ,x.free-calls
                    print(,"GABLE CALLS  "),x.ge_calls
                    print("DEBITS          "),x.debits

                    print("TAXES           "),x.tax
                    print("GROSS AMOUNT    "),x.gross_amt
                    print(" SELF. CREDITS         "),x.credits
                    print("RENTAL                             "),x.rent
                    print("AMOUNT PAYABLE IF PAID ON OR BEFORE "),x.net_amt_bef
                    print(" SELF. SURGE                           "),x.surge
                    print("AMOUNT PAYABLE IF PAID ON OR AFTER  "),x.net_amt_aft
                    break
            else:
              print"Record not found"
#main
    ppass=raw_input("ENTER THE PASSWORD::")
    if(ppass!=”HELLO”):
        
    	print("INVALID PASSWORD")
               exit
    
        print("ENTER YOUR CHOICE:-")
        print("PRESS 1:TO ADD NEW RECORD")
        print("PRESS 2:TO SEE THE RECORDS")
        print("PRESS 3:FOR ENQUIRY")
        print("PRESS 4:FOR MODIFICATION")
        print("PRESS 5:FOR EXIT")
        a=int(raw_input(“ENTER CHOICE”))

	    #TO ADD NEW RECORD
if(a==1):
    valid=1
	  while(valid):
		print("ENTER THE RECORD:-")
    		te_no=int(raw_input("TELEPHONE_NO :"))
    
