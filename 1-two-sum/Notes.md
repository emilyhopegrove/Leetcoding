<h2>two-sum Notes</h2><hr>###

# The key idea is to use a hash table to keep track of the elements you've encountered so far in the array, 
#mapping each element's value to its index. 
#Then, for each element \(x\) in the array, you check if the target value minus \(x\) (i.e., \(target - x\)) exists 
#in the hash table. If it does, you've found the two numbers that add up to the target, and you can return their 
#indices immediately. This approach only requires a single pass through the array, hence the \(O(n)\) time complexity.

# Here's a brief outline of the algorithm with a focus on achieving better than \(O(n^2)\) time complexity:

# 1. **Initialize a hash table** to store the value and index of each element as you iterate through the array.

# 2. **Iterate through the array once**:
#    - For each element \(x\), calculate the complement \(y = target - x\).
#    - Check if \(y\) exists in the hash table.
#      - If \(y\) is found, return the current index and the index of \(y\) from the hash table as the solution.
#      - If \(y\) is not found, add \(x\) along with its index to the hash table.

# 3. **If no solution is found during the iteration**, it means there are no two numbers in the array that add up to the target.

# This algorithm efficiently finds the required indices without needing to compare each element with every other element, thus avoiding the \(O(n^2)\) time complexity associated with the brute force approach.


###