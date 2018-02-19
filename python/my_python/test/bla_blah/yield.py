# Generator is the construct of a function or codes it won't do anything unless 
#you activate it with for or next() until it is empty
def create_generator(a, b):
    list = range(2)
    # return the first value of the loop and then keep returning the next value from the next call
    c = 1
    print "You'll only see this once" 
    for x in list:
        print c
        c += 1
        yield a, b
    yield [a, b, c]
    #generator will be empty if it won't hit yield anymore and finished. Thanks to yield you can 
    # continue the function after returning the value

word = 'Hello'
mygene = create_generator(word, input('input something:\n'))

for i in mygene:
    print i
