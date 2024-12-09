dict1 = {}
total = 0
no_subj = int(input("enter the total number of subjects:"))
print("enter the details:")
for i in range(no_subj):
    key = input("enter the subject names:")
    value = int(input("Marks obtained:"))
    dict1[key] = value
print("Subjects and Marks details entered:")
print(dict1)
for j in dict1.values():
    total = total + j
    print("total:", total)
perc = (total / (no_subj * 100)) * 100
print("percentage:", perc)
if perc <= 100 and perc >= 80:
    print("Grade A+")
elif perc <= 81 and perc >= 60:
    print("Grade A")
elif perc <= 61 and perc >= 40:
    print("Grade C")




