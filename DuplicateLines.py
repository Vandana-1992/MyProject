# creating the output file
outputFile = open('C:\\Users\\VandanaT\\PycharmProjects\\pythonProject\\Practice Folder\\output file', "w")

# reading the input file
inputFile = open('C:\\Users\\VandanaT\\PycharmProjects\\pythonProject\\Practice Folder\\samplefile', 'r')

# holds lines already seen
lines_seen_so_far = set()

# iterating each line in the file
for i in inputFile:

    # checking if line is unique
    if i not in lines_seen_so_far:
        # write unique lines in output file
        outputFile.write(i)

        # adds unique lines to lines_seen_so_far
        lines_seen_so_far.add(i)

# closing the file
inputFile.close()
outputFile.close()






