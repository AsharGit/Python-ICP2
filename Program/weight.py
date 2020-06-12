alist = []
blist = []

# Get number of students from user
num = int(input("How many students?:"))

# Random weight generated for students
for i in range(num):
    weight = int(input("Please enter weight in lbs:"))
    alist.append(weight)

# Print weight in lbs and convert to kg for another list
print("\nWeights in pounds:")
for i in alist:
    print(str(i) + " lbs")
    lbstokg = round((i/2.205), 2)
    blist.append(lbstokg)

# Print weight in kg
print("\nWeights in kgs:")
for i in blist:
    print(str(i) + " kg")