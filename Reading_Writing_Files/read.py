# Reading Files
#This exercise  opens a text file in the script and prints it out.

from sys import argv

script, filename = argv

txt = open(filename) #open the file

print("Here's your file %r:" % filename)

print(txt.read()) # read  and print the  contents of the  file

print("type the filename again:")

file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

#################################################
# Here is an example text file:
# This is stuff I typed into a file.
# It is really cool stuff.
#
# To run the script type: python read.py example.txt
#You get the following output
#
#Here's your file 'example.txt':
#This is stuff I typed into a file.
#It is really cool stuff.
#
#Next type the file again
#type the filename again:
#>example.txt
#This is stuff I typed into a file.
#It is really cool stuff.
