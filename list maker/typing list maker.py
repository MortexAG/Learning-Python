import texttable
from texttable import Texttable
# To Import The Name
print("PLease Enter Your name")
imported_name = input()
namesfile = open('list maker/imported_names.txt', 'a')
namesfile.write(imported_name)
namesfile.write('\n')
namesfile = open('list maker/imported_names.txt', 'r')
name = namesfile.read()
namesfile.close()
# To Import the Age
print("PLease Enter Your Age")
imported_age = input()
agesfile = open('list maker/imported_ages.txt', 'a')
agesfile.write(imported_age)
agesfile.write('\n')
agesfile = open('list maker/imported_ages.txt', 'r')
age = agesfile.read()
agesfile.close()

# To Import The Career
print("Please Enter Your Career")
imported_career = input()
careersfile = open('list maker/imported_career.txt', 'a')
careersfile.write(imported_career)
careersfile.write('\n')
careersfile = open('list maker/imported_career.txt', 'r')
career = careersfile.read()
careersfile.close()


# To Make the List

list = [["Name", "Age", "Career"], [name, age, career]]

table = Texttable()
table.add_rows(list)
print(table.draw())

# To Keep it Open

# no need for now
