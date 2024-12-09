import os.path
def pref_fun(str_new):
    print(os.path.commonprefix(str_new))

str1 = ["flower", "flow", "flight"]
pref_fun(str1)