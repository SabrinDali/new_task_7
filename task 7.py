# Q1
name = ["Tarteel", "Asmaa", "Ahmed"]

# a)
name.insert(0, "Sabrin")
print(name)

# b)
name.pop()
print(name)

# c)
name.append("Hamda")
print(name)

# d)
del name[2]
print(name)



# Q2
friends = ["Adel", "Ahmed"]
employees = ["Samah", "Amjad"]
school = ["Ali", "Basma"]

joined_list = []
joined_list.extend(friends)
joined_list.extend(employees)
joined_list.extend(school)

print(joined_list)


# Q3
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

result_dict = dict1.copy()
result_dict.update(dict2)
result_dict.update(dict3)

print(result_dict)


# Q4
my_dict = {}

for num in range(1, 16):
    my_dict[num] = num ** 2

print(my_dict)


# Q5
dict1 = {"a": 100, "b": 200, "c": 300}
dict2 = {"a": 150, "b": 200, "d": 400}

combined_dict = dict1.copy()  # Create a copy of dict1

for key, value in dict2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print(combined_dict)


# Q6
list1 = ["Ten", "Twenty", "Thirty"]
list2 = [10, 20, 30]

result_dict = {}
for key in dict1.keys() | dict2.keys():
    result_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(result_dict)

# Q7
sampleDict = {
    "class": {
        "student": {
            "name": "mike",
            "mark": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

output = sampleDict["class"]["student"]["mark"]["history"]

print(output)


# Q8
myDict = {
    1: "Alaa",
    5: "Hadeel",
    7: "Hanin",
    13: "Malak",
}

# Print values for keys less than 10
value_key = "->".join(
                    value for key, value in myDict.items()
                        if key < 10
                    )

print(value_key)
