# IT/ICT Student Percentage

# Program Requirements:
# 1. Find the number of IT/ICT students in class
# 2. Calculate IT/ICT Students Percentage
# 3. Must use float data type (to facilitate right-alignment)
# 4. Format, right-alignment numbers, round to two decimal places

it_stds = float(input("Enter the number of IT students: "))
ict_stds = float(input("Enter the number of ICT students: "))

total_stds = it_stds + ict_stds

it_percent = (it_stds / total_stds) * 100
ict_percent = (ict_stds / total_stds) * 100

print(f"{'Total students:':20} {total_stds:10.2f}")
print(f"{'IT students %:':20} {it_percent:10.2f}%")
print(f"{'ICT students %:':20} {ict_percent:10.2f}%")
