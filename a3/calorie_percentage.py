# Calorie Percentage
# Program Requirements:
# 1. Find calories per grams of fat, carbs, and protein.
# 2. Calculate percentages.
# 3. Must use float data types.
# 4. Format, right-align numbers, and round to two decimal places.

# 1 gram of fat = 9 calories
# 1 gram of carbs = 4 calories
# 1 gram of protein = 4 calories

# Input
fat_grams = float(input("Enter total fat grams: "))
carb_grams = float(input("Enter total carb grams: "))
protein_grams = float(input("Enter total protein grams: "))

# Calculations
fat_calories = fat_grams * 9
carb_calories = carb_grams * 4
protein_calories = protein_grams * 4

total_calories = fat_calories + carb_calories + protein_calories

fat_percent = (fat_calories / total_calories) * 100
carb_percent = (carb_calories / total_calories) * 100
protein_percent = (protein_calories / total_calories) * 100

# Output
print("\n{:<10s}{:>15s}{:>15s}".format("Type", "Calories", "Percentage"))
print("{:<10s}{:>15.2f}{:>14.2f}%".format("Fat", fat_calories, fat_percent))
print("{:<10s}{:>15.2f}{:>14.2f}%".format("Carbs", carb_calories, carb_percent))
print("{:<10s}{:>15.2f}{:>14.2f}%".format("Protein", protein_calories, protein_percent))
