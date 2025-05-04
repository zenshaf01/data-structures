"""
Binary Search Range:

You may encounter questions where the question gives you a range instead of an array. And along with the range you might be given a criteria to apply to e range to guess the correct number.
"""
class Solution(object):
    pick = 6
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if self.guess(mid) > 0:
                low = mid + 1
            elif self.guess(mid) < 0:
                high = mid - 1
            else:
                return mid
        return -1
    
    def guess(self, n):
        if n > self.pick:
            return -1
        elif n < self.pick:
            return 1
        else:
            return 0