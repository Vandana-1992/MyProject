import re
f = open("C:\\Users\\VandanaT\\PycharmProjects\\pythonProject\\Practice Folder\\samplefile", 'r')
content = f.read()
content = content.split()
print(content)
for i in content:
    pattern = re.compile(r"\b\w{10}\b")
    if bool(pattern.match(i)):
        print("valid phone number is:", i)