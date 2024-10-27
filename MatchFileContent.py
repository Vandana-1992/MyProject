f = open("C:\\Users\\VandanaT\\PycharmProjects\\pythonProject\\Practice Folder\\extrafile", "r")
x = f.readline()
#x= x.split()
print("i/p given:", x)
num = input("enter a output got from server:")
if num in x:
    print("match found:")
else:
    print("no match")

f.close()
