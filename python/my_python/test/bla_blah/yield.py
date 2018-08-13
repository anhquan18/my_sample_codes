# Generator is the construct of a function or codes it won't do anything unless 
#you activate it with for or next() until it is empty
def create_generator(a, b):
    list = range(input('>> '))
    # return the first value of the loop and then keep returning the next value from the next call
    c = 1
    print "You'll only see this once" 
    try:
        for x in list:
            print 'inside loop,', c
            c += 1
            yield a, b
        '''while True:
            yield [a, c]
            print 'after for loop'''
    finally:
        print 'bottom of generator'
    #generator will be empty if it won't hit yield anymore and finished. Thanks to yield you can 
    # continue the function after returning the value
    # you can use:
    # while True: to run the generator forever

word = 'Hello'
mygene = create_generator(word, input('input something: '))

for i in mygene:
    print  'yay'

print 'outside loop,', i
print i
# after the generator totally finished, if you call it on more time it will only return the last yield and no longer run anything after the yield

print create_generator('Hi',10)
print create_generator('Hi',5)
print create_generator('Hi',1)
