states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[5])
print(states_of_america[1])
#
# num_of_states = len(states_of_america) # 50 -1
# #print(num_of_states)
# print(states_of_america[num_of_states - 1])


# Nested Lists, inserting two lists into one

fruits = ["cherry", "Apple", "Pear", "Mango" ]
veg = ["Cucumber", "Kale", "Spinach", "Green"]

dirty_dozen =[fruits, veg]

user = int(input("Input a nuber of 0 to 1: \n"))
print(dirty_dozen[user]) #we are asking the user to put in the number
print(dirty_dozen[0]) #we are doing it manually
# print(dirty_dozen[1][-2])
# print(dirty_dozen[1])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

