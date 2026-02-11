# data = []

# inpout_data1 = input("Enter any data: ")
# inpout_data2 = input("Enter any data: ")
# inpout_data3 = input("Enter any data: ")


# data.append(inpout_data1)
# data.append(inpout_data2)
# data.append(inpout_data3)


# print(data)



# fruits = ['apple', 'pear', 'melon']
# new_fruit = input("Enter any fruit")

# fruits.insert(2, new_fruit)
# print(fruits)


# def name_age(name, age):
#     return f"my name is {name} and i am {age} years old"

# print(name_age("gvanca", 15))

# def square(num):
#     return num ** 2

# print(square(2))


# twice_list = []
# def twice (list):
#     for i in list:
#       twice_list.append(i * 2)
#     return twice_list
# print(twice([2, 3, 4, 6, 7, 9]))


# new_lst = []
# def square (list):
#     for i in list:
#             new_lst.append(i ** 2)
#     return new_lst
    
# print(square([2, 4, 6, 7]))

reversed = []

def spin_words(sentence):
    split_list = sentence.split()
    for i in split_list:
        reversed.append(i[::-1])
    return " ".join(reversed)

print(spin_words("Hi my name is gvanca"))


