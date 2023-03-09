# CTI-110 #
# P2HW2 - List #
# Harmony Lewis #
# 3/9/2023 #
#

# Step 1. Ask User for Grades #
grade1 = float(input("Enter grade for Module 1:"))
grade2 = float(input("Enter grade for Module 2:"))
grade3 = float(input("Enter grade for Module 3:"))
grade4 = float(input("Enter grade for Module 4:"))
grade5 = float(input("Enter grade for Module 5:"))
grade6 = float(input("Enter grade for Module 6:"))

# List #
gradeList = [grade1, grade2, grade3, grade4, grade5, grade6]

# Print Statements #
print("Enter grade for Module 1:", grade1)
print("Enter grade for Module 2:", grade2)
print("Enter grade for Module 3:", grade3)
print("Enter grade for Module 4:", grade4)
print("Enter grade for Module 5:", grade5)
print("Enter grade for Module 6:", grade6)

# Results Print Statements #
print("-" * 12, "Results", "-" * 12)
print("Lowest Grade:", "\t", "\t", min(gradeList))
print("Highest Grade:", "\t", "\t", max(gradeList))
print("Sum of Grades:", "\t", "\t", sum(gradeList))
print("Average:", "\t", "\t", sum(gradeList)/len(gradeList))
print("-" * 40)



