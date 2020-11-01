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
###output will also be 'None' but 'addresses' list's itself sorted
print(addresses.sort())
###output will be alphabetically sorted addresses list
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
