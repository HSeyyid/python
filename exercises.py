### Exercise 1 ###

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
#printing as many element we want at the same time
print(last_element, element5)

### Exercise 2 ###

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
### output will be 'None', however cities list will be sorted. if we use sorted() function to sort, output will be sorted list 'sorted_cities' although 'cities' list is not sorted. It is because sorted() function returns a sorted list value but does not change the original list 
print(sorted_cities)
### output will also be 'None' but 'addresses' list's itself sorted
print(addresses.sort())
### output will be alphabetically sorted addresses list
print(addresses)

### Exercise 3 ###

def dave_check(user_name):
  if user_name == "Dave":
    #print("Get off my computer Dave!")
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
    #print("I know it is you Dave! Go away!")
    return "I know it is you Dave! Go away!"
  
# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

#dave_check(user_name)
print(dave_check(user_name))

### Exercise 4 ###
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

size_of_poetry = 6

while size_of_poetry > 0:
  #pop() function retrieves and returns an element from the end of a list, then removes it from the list
  students_in_poetry.append(all_students.pop())   
  size_of_poetry += -1

print(students_in_poetry)

### Exercise 5 ###

#List Comprehension
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

#if there is an if/else clause, then put the if/else in front of the for statement else vise verse
#The if/else is placed in front of the for component of the list comprehension.
#The left side of statement is 'action will be occured' according to result of right side's execution
divbythree = ["Yes" if number % 3 == 0 else "No" for number in range(1,20)]
print(divbythree)

### Exercise 6 ###
#Write your function here
def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst.pop(0)
    if len(lst) == 0:
      return []
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

### Exercise 7 ###
#Write your function here
def odd_indices(lst):
  odd_indexed_lst = []
  length = len(lst)
  i = 1
  while i < length:
    odd_indexed_lst.append(lst[i])
    i += 2

  return odd_indexed_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
print(odd_indices([4]))

### Exercise 8 ###

#Write your function here
def exponents(bases, powers):
  raised_list = []
  for base in bases:
    for power in powers:
      raised_list.append(base**power)
  
  return raised_list

#Uncomment the line below when your function is done
print(exponents([0, 3, 4], [0, 2, 3]))

### Exercise 9 ###

#Write your function here
def reversed_list(lst1, lst2):
  length  = len(lst1)
  i = 0
  while i < length:
    if lst1[i] != lst2[length - (i+1)]:
      return False
    i += 1
  return True
  
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
