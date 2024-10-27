#from os.path import commonprefix
new_str = ""
count = 0
strs = ["flower", "flow", "flight"]
strs = sorted(strs, key = len)
print(strs)
    #new_str = commonprefix(strs)
    #print(new_str)
for i in strs:
    minim = int(min(len(strs[i], len(strs[i+1]))))
    for j in range(0,minim):
        if strs[i][j] == strs[i+1][j]:
            count = count + 1
prefix = strs[0] [0:count]
print(prefix)
















