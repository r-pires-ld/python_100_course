
print('Tip calculator')
tip_perc = float(input("How much do you want to give as tip? "))
bill=float(input("Value of the bill? $"))
split=int(input("Split the bill with how many people? "))


total_bill = (((bill*tip_perc)/100)+bill)/split
print(f"The total amount for each person is: ${total_bill:.2f}")