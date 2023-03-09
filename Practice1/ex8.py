formatter = "%r %r %r %r"
print(formatter % (1,2,3,4)) #1 2 3 4
print(formatter % ("one","two","three","four")) #'one' 'two' 'three' 'four'
print(formatter % (True, False, False, True)) #'one' 'two' 'three' 'four'