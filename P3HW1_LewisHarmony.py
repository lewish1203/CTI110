# This program takes a number grade , determines average and displays letter grade for average. #
# 3/20/23 #
# CTI-110 P3HW1 - Debugging #
# Harmony Lewis #



# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1:'))
mod_2 = float(input('Enter grade for Module 2:'))
mod_3 = float(input('Enter grade for Module 3:'))
mod_4 = float(input('Enter grade for Module 4:'))
mod_5 = float(input('Enter grade for Module 5:'))
mod_6 = float(input('Enter grade for Module 6:'))

# Add grades entered to a list #
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: Determine lowest, highest , sum and average for grades #
low = min(grades)
max = max(grades)
sum = sum(grades)
average = sum / 6
print("-" * 12, "Results", "-" * 12)
print("Lowest Grade: ", "\t", "\t", round(low, 2))
print("Highest Grade: ", "\t", round(max, 2))
print("Sum of Grades: ", "\t", round(sum, 2))
print("Average: ", "\t", "\t", round(average, 2))
print("-" * 40)

# Determine letter grade for average #
if average >= 90:
    print('Your grade is: A')
elif average >= 80:   
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') 





