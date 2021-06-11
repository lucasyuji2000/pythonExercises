class Stack: # defining the stack class
    def __init__(self): # defining the constructor function
        self.__stk = [] # __ private

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack): # subclass
    def __init__(self):
        Stack.__init__(self) #invoke a superclass constructor
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        val = Stack.pop(self)
        self.__counter += val



stk = CountingStack() # instantianting the object

for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())