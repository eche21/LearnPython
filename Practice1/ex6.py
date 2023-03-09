#Strings, variables and formats
##########################################
#The %r is best for debugging, and
# You should use %s for formatting and only use %r for getting debugging information about something.
# The %r  will give you the “raw programmer’s” version of variable, also known as the “representation.”he other formats are for actually displaying variables to users
#
x = "there are %d types of people." % 10
print(x)
#there are 10 types of people.

#################################
binary = "binary"
do_not = "don't"
y= "those who know %s and those who %s." % (binary, do_not)
print(y)
#those who know binary and those who don't.

#######################################
print("I said: %r." % x)
#I said: 'there are 10 types of people.'.

#########################################
print(binary + do_not)
#binarydon't

#############################################
print("." *10)
#..........