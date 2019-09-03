# Given the following dictionary, representing a mapping from names to phone numbers:
#
# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }
#
# Write code to do the following:
#
# 1. Print Elizabeth's phone number.
# 2. Add an entry to the dictionary: Kareem's number is 938-489-1234.
# 3. Delete Alice's phone number.
# 4. Change Bob's phone number to '968-345-2345'.
# 5. Print all the phone entries.

phonebook_dict = {
   'Alice': '703-493-1834',   
   'Bob': '857-384-1234',
   'Elizabeth': '484-584-2923'
 }
print(f'Original Dictionary {phonebook_dict}')

# Print Elizabeth's phone number.
for key, value in phonebook_dict.items():
    if key == "Elizabeth":
        print(f'{key} \'s phone number is {value}')

# Add an entry to the dictionary
phonebook_dict['Kareem'] = '938-489-1234'


# Delete Alice's phone number
phonebook_dict.pop("Alice")


# Change Bob's phone number
phonebook_dict['Bob'] = '968-345-2345'

# Print all the phone entries
for key, value in phonebook_dict.items():
    print(f'{key} : {value}')

