"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

For this solution we are using the following data structures:
1. Hash Map

Trick:
The trick to solve this is to count the num students which will eat each type of sandwic and keep that count in a hash map.
Then iterate over the sandwiches and see if it exist in the count map, If it does decrement it to denote that the stuenden has eaten the lunch and exited the line.
Return the result if a sandwich is found which is not edible by any of the stuends or when we have exhaustewd the sandwiches list.

Algorithm:

1. Count students
2. Count the students that want to eat each type of sandwich (0 or 1) and put it in a map.
3. Start iterating over the sandwich list
4. If sandwich is desired by a student (This will be determined if that sandwich is present in the count map)
5. Decrement the count in the map and the result (represents a student eating the lunch and exiting the line)
6. If a sandwich is encountred which is not (no longer) in the map (value is 0) then retuen the result variable respresenting student who have not eaten lunch
7. If sandwich list is exhausted and we have looked at all sandwiches and not hit the return condition, return the result (represents students who have not eaten lunch)
"""

from collections import Counter

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        result = len(students)
        count = Counter(students)
        
        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
                result -= 1
            else:
                return result
        
        return result