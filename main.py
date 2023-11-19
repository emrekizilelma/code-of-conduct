# In Python how I'm Creating a new variables? Just doing this.
# I'm prefer to using snake_case style which also i am also using in C.
# Some variables can be short, for example using "var" instead "variable" which makes sense.

variable = "something" # For strings
variable_1 = 10        # For integers

def fun_1(commands):  # fun_1 can be reading as a "Function 1". Again snake_case.
    return True       # We have to be careful when we are coding because coding is like art. It's have to be beatiful. 
                      # Also it's increasing to readability. Which is really important for community projects.

fun_1()                # Classic calling any function is be like.

class Person:         # Class name is must be starting with big letter like "Person" or "Example". Why? Why not? Class is really specific things so thats which makes to sense using it.
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)