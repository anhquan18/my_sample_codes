class who:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # call out the exception by yourself
        if b == 0:
            raise ZeroDivisionError

me = who(1,2)
you = who(1,0) 
