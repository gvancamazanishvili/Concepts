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

# reversed = []

# def spin_words(sentence):
#     split_list = sentence.split()
#     for i in split_list:
#         reversed.append(i[::-1])
#     return " ".join(reversed)

# print(spin_words("Hi my name is gvanca"))




# for i in range(1, 10, 1):
#     print(i)

# for i in range(1, 20, 2):
#     print(i)


#  FOR LOOP 
# რიცხვების დაბეჭდვა: დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 1-დან 10-მდე.

# ლუწი რიცხვები: დაბეჭდე ყველა ლუწი რიცხვი 1-დან 20-მდე.

# კენტი რიცხვები: დაბეჭდე ყველა კენტი რიცხვი 1-დან 15-მდე.

# for i in range(1, 15, 2):
#     print(i)


# შებრუნებული თანმიმდევრობა: დაბეჭდე რიცხვები 10-დან 1-მდე კლებადობით.

# for i in range(10, 1, -1):
#     print(i)

# გამრავლების ტაბულა: მოცემული რიცხვის (მაგ. 5) გამრავლების ტაბულა 1-დან 10-მდე.

# for i in range(1 ,10, 1):
#     print(i * 5)

# სიის ელემენტები: გაქვს სია ["ვაშლი", "ბანანი", "ატამი", "ფორთოხალი"]. დაბეჭდე ყველა ელემენტი.

# lst = ["ვაშლი", "ბანანი", "ატამი", "ფორთოხალი"]

# for i in lst:
#     print(i)

# სტრიქონის სიმბოლოები: მოცემული სტრიქონის თითოეული სიმბოლო დაბეჭდე ცალ-ცალკე ხაზზე.

# word  = "I love Goa"
# for i in word:
#     print(i)

# რიცხვების ჯამი: გამოთვალე და დაბეჭდე 1-დან 100-მდე ყველა რიცხვის ჯამი.
# sum = 0

# for i in range(1, 100, 1):
#     sum += i
# print(sum)

# ფაქტორიალი: მოცემული რიცხვის (მაგ. 6) ფაქტორიალის გამოთვლა.


# ----------------------------------------------------------------------------------------------------------------------------------


# რიცხვების კვადრატები: დაბეჭდე 1-დან 10-მდე თითოეული რიცხვის კვადრატი.

# for i in range(1, 10,1):
#     print(i ** 2)

# სიაში ძებნა: გაქვს სია [10, 25, 30, 45, 50]. დაბეჭდე ყველა რიცხვი, რომელიც 30-ზე მეტია.

# nums = [10, 25, 30, 45, 50]

# for i in nums:
#     if i > 30:
#         print(i)

# სიმბოლოების დათვლა: მოცემულ სტრიქონში დაითვალე, რამდენჯერ გვხვდება კონკრეტული სიმბოლო (მაგ. "a").

# word1 = "Mamamia"

# for i in word1:
#     count = word1.count('m')
#     print(count)

# რიცხვების უკუქცევა: სიაში [1, 2, 3, 4, 5] შექმენი ახალი სია უკუქცევითი თანმიმდევრობით.

# nums =  [1, 2, 3, 4, 5]

# for i in nums:
# #     rev_lst = nums[::-1]
# #     new_lst.append(rev_lst)
# # print(new_lst)
#     print(nums[::-1])

# print(new_lst)
# დივიზორები: მოცემული რიცხვის (მაგ. 24) ყველა დელიკატის პოვნა და დაბეჭდვა.

# --------------------------------------------------------------------------------------------------------

# მარტივი რიცხვების პოვნა: იპოვე და დაბეჭდე ყველა მარტივი რიცხვი 1-დან 50-მდე.

for i in range(1, 50, 1):
    if i % i == 0 and i % 1 == 0:
        print(i)


# ფიბონაჩის მიმდევრობა: დაბეჭდე ფიბონაჩის მიმდევრობის პირველი 15 რიცხვი.


# -----------------------------------------------------------------------------------------------------



# სიის გაფილტვრა: გაქვს სია [-5, 10, -3, 8, -1, 15]. შექმენი ახალი სია მხოლოდ დადებითი რიცხვებით.


# lst = [-5, 10, -3, 8, -1, 15] 
# new_lst = []

# for i in lst:
#     if i > 0:
#         new_lst.append(i)
# print(new_lst)

# პალინდრომის შემოწმება: შეამოწმე, არის თუ არა მოცემული სტრიქონი პალინდრომი (იგივეს კითხულობს ორივე მიმართულებით).


# --------------------------------------------------------------------------------------------------------


# სიაში უნიკალური ელემენტები: გაქვს სია [1, 2, 2, 3, 4, 4, 5]. დაბეჭდე მხოლოდ უნიკალური ელემენტები.

# lst =  [1, 2, 2, 3, 4, 4, 5]
# print(set(lst))


# რიცხვთა თამაში FizzBuzz: 1-დან 30-მდე დაბეჭდე რიცხვები, მაგრამ 3-ის ჯერადებისთვის დაბეჭდე "Fizz", 5-ის ჯერადებისთვის "Buzz", ხოლო 15-ის ჯერადებისთვის "FizzBuzz".

# for i  in range(1, 40, 1):
#     if i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 15 == 0:
#         print("FizzBuzz")