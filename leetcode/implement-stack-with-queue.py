"""
https://leetcode.com/problems/implement-stack-using-queues/submissions/1430817216/

The trick to implement a stack (LIFO) data structure with a queue (FIFO) data strcuture is to make sure to adhere to the LIFO rule for the stack

time complexity:
Push: O(1)
Empty: O(1)
Top: O(1)
Pop: O(n) -> This is because we would have to iterate over the queue to bring the last element added to the front and then remove it since in a stack have to pop the last value added.
Stack -> Add to right and remove from right
Queue -> Add to right and remove from left
"""

from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.queue) - 1):
            # bring each value on the left to right except the last value which wer have to pop
            self.push(self.queue.popleft())
        # pop and return the value at left now which was the right most before the shifts
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()