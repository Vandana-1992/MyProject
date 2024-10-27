usr_dict = {}
total_marks = 0
total_sub = int(input("enter the number of subjects:"))
print("enter the marks obtained in all the subjects:")
for i in range(total_sub):
    key = input("enter the subject name:")
    value = int(input("enter the marks obtained:"))
    usr_dict[key] = value
print("Marks obtained:", usr_dict)
print("total marks obtained is:")
for i in usr_dict.values():
    total_marks = total_marks + i
print(total_marks)
average1 = float(total_marks / total_sub)
print("average:", average1)
if average1 >= 85 and average1 <= 100:
    print("Passed with grade A+")
elif average1 >= 75 and average1 <= 84:
    print("Passed with grade A")
elif average1 >= 60 and average1 <= 74:
    print("Passed with grade B+")
elif average1 >= 40.0 and average1 <= 59:
    print("Passed with grade B")
else:
    print("Fail:Grade C")



