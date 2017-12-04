# truthiness
# Empty list and array all are considered as false in python.
# A custom types

class Aclass:
    """
    Testing the trutiness in Python
    """
    def __init__(self):
        self.data = []


    def add(self, item):
        self.data.append(item)

    def __bool__(self):
        return True if self.data else False


a = Aclass()
print(a)
b = a.add('Thing')
print("Print if somthing in list", b)



# Print the Trutiness

def print_truthiness(msg,exp):
    print(('True' if exp else 'False'))
print_truthiness("Testing", 3)
print_truthiness('None','')
# we can figure out nothing in list means its false
