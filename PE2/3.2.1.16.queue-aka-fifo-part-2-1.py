#!/usr/bin/env python3

# 3.2.1.16 Queue aka FIFO: part 2
# 
# Your task is to slightly extend the Queue class' capabilities.
# We want it to have a parameterless method that returns True if the queue is empty and False otherwise.
# 
# Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.
# 
# Expected output
# 
# 1
# dog
# False
# Queue empty


class QueueError(IndexError):
    pass


class Queue:
    # Code from the previous lab.
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        if len(self.__queue) > 0:
            return self.__queue.pop(0)
        else:
            raise QueueError
          
    def getQueue(self):
        # added now to get the private queue
        return self.__queue


class SuperQueue(Queue):
    def __init__(self):
        super().__init__()
        
    def isempty(self):
        return len(self.getQueue()) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
