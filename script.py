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
print(sorted_cities)
print(addresses.sort())
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
