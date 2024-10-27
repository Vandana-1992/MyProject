def anagram_fun(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        string1 = string1.lower()
        string2 = string2.lower()
        if sorted(string1) == sorted(string2):
            return True

str1 = input("Enter a first string: ")
str2 = input("Enter a second string: ")
res = bool(anagram_fun(str1, str2))
if res:
    print("2 strings are anagrams:")
else:
    print("2 strings are not anagrams:")