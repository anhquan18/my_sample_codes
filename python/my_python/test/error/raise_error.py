class ActionCancel(Exception):
    def __str__(self):
        return self.__class__.__name__

try:
    raise ActionCancel()
except Exception as er:
    print er

