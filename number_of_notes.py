value=int(input("amount of dollars "))
bills_100=value//100
bills_10=(value%100)//10
bills_1=((value%100)%10)//1
print("number of hundred bills",bills_100,"number of ten bills",bills_10,"number of one bills",bills_1)