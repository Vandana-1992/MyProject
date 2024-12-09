def pref_fun(str_new):
    if len(str_new) == 0:
        print("")
    elif len(str_new) == 1:
        print("prefix:", str_new)
    else:
        str_new = sorted(str_new, key=len)
        print("After sorting:", str_new)
        tmp = ""
        first = str_new[0]
        last = str_new[len(str_new) - 1]
        for i in range(len(str_new)):
            if first[i] == last[i]:
                tmp = tmp + first[i]
        print("prefix:", tmp)

str1 = ["hello", "height", "herry", "help"]
pref_fun(str1)