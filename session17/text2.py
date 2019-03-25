import json
import termcolor

# -- Open the json file
f = open("person1.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person1 = json.load(f)

# Print the information in the object
print()
termcolor.cprint("Name: ", 'green', end="")
print(person1['Firstname'], person1['Lastname'])

termcolor.cprint("Age: ", 'green', end="")
print(person1['age'])

# Get the phoneNumber list
phoneNumbers = person1['phoneNumber']

# Print the number of elements int the list
termcolor.cprint("Phone numbers: ", 'green', end='')
print(len(phoneNumbers))

# Print all the numbers
for i, num in enumerate(phoneNumbers):
    termcolor.cprint("  Phone {}:".format(i), 'blue', end='')
    print(num)