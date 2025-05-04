"""
Search 2d matrix

The trick is to apply binary search on the outer array first and then apply it on inner array Which will bring the time complexity to be log (m*n)
First apply binary search to find the row in which the target might be in based on order
Then apply binary search to the found row in the previous step to determine if the target is in the selected row.

1   |     2     | 4     <- Top
5   |     6     | 8
10  |     12    | 13    <- Bottom
"""

def search_2d_matrix(matrix, target):
    # Figure out the rows and columns in the matrix
    rows, cols = len(matrix), len(matrix[0])

    # apply binary search to outer array to figure out the row in which the target might be
    top, bottom = 0, rows - 1

    # keep selection and check rows to find the target row 
    # (We need the top and bottom to be specific popinters to access the target row after this loop)
    while top <= bottom:
        # select a middle row
        row = (top + bottom) // 2
        # if target is greater than the last element of this row then move the top 1 index down
        if target > matrix[row][-1]:
            top = row + 1
        # if target is less than the first element of the row than move the bottom 1 index up
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    
    # if the top and bottom are not correct means we did not dinf a row which might have the target than return false meaning the target is not in matrix.
    if not (top <= bottom):
        return False
    
    # select the target row
    row = (top + bottom) // 2
    # set the left and right pointers
    l, r = 0, cols - 1

    # while the left and right have not met
    while l <= r:
        # select middle
        m = (l + r) // 2
        # if target is larger than middle than move left to middle + 1
        if target > matrix[row][m]:
            l = m + 1
        # if target is less than middle than move right middle - 1
        elif target < matrix[row][m]:
            r = m - 1
        # we have found the target
        else:
            return True
        
    # if execution gets here means we did not find our target in the selected row    
    return False