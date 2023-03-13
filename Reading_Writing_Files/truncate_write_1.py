#This code truncates and writes to a text file if you want do want to erase the file.

from sys import argv

script, filename = argv

print("we're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

##############################################
#EXAMPLE
#
# python truncate_write_1.py test.txt
#we're going to erase 'test.txt'.
#If you don't want that, hit CTRL-C (^C).
#If you do want that, hit RETURN.
#?
#Opening the file...
#Truncating the file. Goodbye!
#Now I'm going to ask for three lines.
#line 1: Mary had a little lamb.
#line 2: It's fleece was white as snow.
#line 3: It was also tasty.
#I'm going to write these to the file.
#And finally, we close it.

