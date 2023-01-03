# Given an array of nums, you are given k operations which consist of incrementing one element by one.
# Find the maximum amount of equal elements you can have after k operations.


# Idea: sliding window. Sort nums, then make an array which has the differences between each element.
# The window will only expand, and the window size will be the output.
# The idea is to find the amount of operations it takes to make elements within the window the same.
# Expanding the window will cost the width of the window times the difference on the rightmost pair.

# Moving the window to the right will subtract the operations performed on the leftmost element, or sum
# of all elements in the window. A variable is used to store this. Then, add window * next difference.

# If the number of operations is less than k, update output value to size of window.

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff = []
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i-1])
        if not len(diff): return 1

        o, l, r, total, prev = 1, 0, 0, diff[0], diff[0]
        while r < len(diff):
            if total <= k: 
                o = r - l + 2
                r += 1
            else:
                r += 1
                l += 1
                total -= prev
                prev -= diff[l-1]
            if r < len(diff):
                prev += diff[r] 
                total += (r - l + 1)*diff[r]
        return o