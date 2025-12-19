buying_cost=float(input("please enter price of the product "))
selling_cost=float(input("please enter selling price of product "))
selling_cost*=100
buying_cost*=100
if(buying_cost<selling_cost):
    profit=selling_cost-buying_cost
    profit/=100
    print("profit = ",profit)
else:
    print("no profit")