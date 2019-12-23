class stack:
 #constructor
    def __init__(self):
        self.__stack = [] # create private stack
 #methods
    def pop(self): #pop the item
        if len(self.__stack) < 1:
            return None
        return self.__stack.pop()
    def peek(self): #peek the item (no removal)
        if len(self.__stack) < 1:
            return None
        return self.__stack[len(self.__stack)-1]
    def push(self, item): #push the item
        self.__stack.append(item)
    def size(self): #return stack size
        return len(self.__stack)
    def __str__(self):
        return str(self.__stack)

#class Queue
class Queue:
    #constructor
    def __init__(self):
         self.__queue = [] # create private queue
     #methods
    def dequeue(self): #remove front item
        if len(self.__queue) < 1:
            return None
        return self.__queue.pop(0)
    def peek(self): #peek the item (no removal)
        if len(self.__queue) < 1:
            return None
        return self.__queue[0]
    def enqueue(self, item): #insert rear item
        self.__queue.append(item)
    def size(self): #return queue size
        return len(self.__queue)
    def __str__(self):
        return str(self.__queue)

mystack=stack()
for i in range(5):
    mystack.push(i+1)
myqueue=Queue()
for i in range(5):
    myqueue.enqueue(mystack.pop())
print(myqueue)

