class ActionCancel(Exception):
    def __str__(self):
        return 'ERROR: '+self.__class__.__name__

try:
    raise ActionCancel()
except ActionCancel as er:
    print er
