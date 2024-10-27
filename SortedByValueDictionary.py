dict1 = {"sahana": 20, "vandana": 12, "sandya": 33, "shanthi": 50}
sorted_dict1 = {key: value for key, value in sorted(dict1.items(), key=lambda item: item[1])}
print(sorted_dict1)