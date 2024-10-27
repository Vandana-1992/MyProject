str_new = ""
str1 = str(input("enter the string:"))
position = int(input("enter the position:"))
str_new = str1[:position]
print("After Split:", str1[position:]+ str_new[::])