import re
file1 = open("C:\\Users\\VandanaT\\PycharmProjects\\PythonPracticeFolder\\Example", "r+")
content = file1.read()
word_new = input("enter the word to replace:")
repl_word = input("enter word to replace with:")
content = re.sub(word_new,repl_word, content)
file1.seek(0)
file1.write(content)
file1.truncate()





