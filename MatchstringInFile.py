with open("C:\\Users\\VandanaT\\PycharmProjects\\PythonPracticeFolder\\InputFile", 'r') as file:
    content = file.readlines()
    linenum = 1
    word = input("enter the word:")
    for line in content:
        word_list = line.split()
        if word in word_list:
            print("exists:", linenum)
        linenum = linenum + 1

file.close()