#Square feet to Acres 

#Program Reqiirements:
#1. Research: number of square feet to acre of land.
#2. Must use float data type for user input & calculation 
#3. Format and round conversion to two decimal places


square_feet =(float(input("Enter square feet:")))

acres = square_feet/43560

print(f"{square_feet:,.2f} square feet = {acres:.2f} acres")