# CTI-110 #
# P4HW1 - Score List #
# Harmony Lewis #
# 4/6/2023 #
#

# Step 1. Ask User for Grades #
p = 1 
s = 0 
scoreList = []
scoreCount = int(input("How many scores do you want to enter? "))
print()
while p <= scoreCount:
    print(f"Enter score #", p, ":", end = " ")
    s = float(int(input()))
    if (s < 0) or (s > 100):
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        print(f"Enter score #", p, "again:", end = " ")
        s = float(int(input()))
        p += 1
    else: 
        p += 1
    scoreList.append(s)
print()
print()
low = min(scoreList)
print(f'------------Results----------')
print(f'Lowest Score  : {low:.1f}')
scoreList.remove(low)
total = sum(scoreList)
average = total / len(scoreList)
print(f'Modified List : {scoreList}')
print(f'Scores Average: {average:.2f}')
if average >= 90:
    print(f'Grade         :  A')
elif average >= 80:
    print(f'Grade         :  B')
elif average >= 70:
    print(f'Grade         :  C')
elif average >= 60:
    print(f'Grade         :  D')
else:
    print(f'Grade         :  F')
print('-' * 30)
    





