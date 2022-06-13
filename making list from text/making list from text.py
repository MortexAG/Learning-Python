import texttable

from texttable import Texttable

namesfile = open('names.txt')
names = namesfile.read()
agesfile = open('list maker/ages.txt')
ages = agesfile.read()
professionsfile = open('professions.txt')
professions = professionsfile.read()
list = [["Name", "Age", "Profession"],[names, ages, professions] ]
table = Texttable()
table.add_rows(list)
print(table.draw())

input("Press Enter To Exit")
