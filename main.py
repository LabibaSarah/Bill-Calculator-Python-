print("Welcome to the tip calculor!")
bill=float(input("What was the total bill? "+"$"))
tip=int(input("How much tip would you like to give? 10,12,or 15?"))
split=int(input("How many people to split the bill?"))
tip_as_percent=tip/100
bill_as_percent=bill*tip_as_percent
total_bill=bill+bill_as_percent
bill_as_person=total_bill/split
final_amount=round(bill_as_person,2)
print(f"Each person should pay: +${final_amount}")