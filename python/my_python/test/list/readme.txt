     You must remember the difference between generator and iterable. 
Iterable save thing on memory and can be used many times. Generator generate
things on the fly and can only be used once( this help you alot if you 
don't want to save things)

Ex: 
Iterable: it = [x*x for x in range(3)]
Generator: ge = (x*x for x in range(3)]

# generator is an object

You can return generator with yield statement
