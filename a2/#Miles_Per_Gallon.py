#Miles Per Gallon

#Program Requirements:

#1. Convert MPG.
#2. Must use float data type for user input and calculation 
#3. Format and round conversion to tow decimal places



miles = float(input("Enter the number of miles driven "))
gallons = float(input("Enter the # of gallons used:"))

    #Caluculation 

mpg = miles/gallons 

print(f"{miles:.2f} miles driven and {gallons:.2f} gallons used = {mpg:.2f} mpg")
#print(f"{miles:2f} miles driven and {gallons:.2f} gallons used = {mpg:.2f} mpg")

