str1 = input("Enter a string that should be paranthesis only: ")
stack = []
length = int(len(str1))
if int(length % 2) == 0:
    for i in range(length):
        if str1[i] == "(":
            stack.append(i)
        elif str1[i] == "{":
            stack.append(i)
        elif str1[i] == "[":
            stack.append(i)
        elif str1[i] == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break
        elif str1[i] == "}":
            if stack[-1] == "{":
                   stack.pop()
            else:
                   stack.append(i)
            break
        elif str1[i] == ")":
            if stack[-1] == "(":
                     stack.pop()
            else:
                     stack.append(i)
                     break
    if len(stack) == 1:
        print("All match not found")
        print("False")
    else:
        print("All match found")
        print("True")
else:
    print("length of the string is odd,so No match")
    print("False")