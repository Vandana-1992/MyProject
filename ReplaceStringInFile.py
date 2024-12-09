import re
file = open("C:\\Users\\VandanaT\\PycharmProjects\\PythonPracticeFolder\\InputFile", 'r+')
content = file.read()
word = input("enter the word:")
new_word = input("Enter new word to replace:")
content = re.sub(word, new_word, content)
#Setting the position to the top of the page to insert data
file.seek(0)
#Writing replaced data in the file
file.write(content)
#Truncating the file size
file.truncate()
file = open("C:\\Users\\VandanaT\\PycharmProjects\\PythonPracticeFolder\\InputFile", 'r+')
new_file = file.read()
print(new_file)
file.close()


