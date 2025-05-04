""" 
This can be implemented two ways. 

1. With a doubly linked list. This solution is reltively slower than the one implemented with arrays.
2. With an Array. this is faster than above because we dont have to traverse the array and can uise array indexing to access the element for back and forward operations.

"""
# Doubly linked list solution
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.cur = ListNode(homepage)
        

    # O(1) -> Assignment in constant time
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next
        
    # O(n) -> Has to traverse through the linked list to the target elements which is n steps behind.
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val
        
    # O(n) -> Has to traverse through the linked list to the target elements which is n steps ahead.
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -=1
        return self.cur.val
    
# Array Implementation
class BrowserHistory:    
    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    # O(1)
    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1

    # O(1)
    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    # O(1)
    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]

