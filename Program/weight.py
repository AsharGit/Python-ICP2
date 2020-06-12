alist = []
blist = []

# Get number of students from user
num = int(input("How many students?:"))

# Ask user for students weight
for i in range(num):
    weight = int(input("Please enter weight in lbs:"))
    alist.append(weight)

# Print weight in lbs and convert to kg for another list
# Using loop:
print("\nWeights in pounds:")
for i in alist:
    print(str(i) + " lbs")
    lbstokg = round((i/2.205), 2)
    blist.append(lbstokg)

# Using list comprehension:
clist = [round((i/2.205), 2) for i in alist]

# Print weight in kg
# Loop
print("\nWeights in kgs using loop:")
for i in blist:
    print(str(i) + " kg")

# List comprehension
print("\nWeights in kgs using list comprehension:")
for i in clist:
    print(str(i) + " kg")