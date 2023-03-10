#prompting and passing

from sys import argv

script, user_name = argv
prompt = '>'

print(" Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")

print("do you like me %s?" % user_name)
likes = input(prompt)

print ("where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer))

# Example usage:
# python ex14.py John
# Hi John, I'm the ex14.py script.
#I'd like to ask you a few questions.
#do you like me John?
#>I do
#where do you live John?
#>Virginia
#What kind of computer do you have?
#>Windows

#Alright, so you said 'I do' about liking me.
#You live in 'Virginia'. Not sure where that is.
#And you have a 'Windows' computer. Nice
