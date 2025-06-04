class Node:
    def __init__(self):
        # Since there are only two possible bits (0 and 1), use a list of size 2
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, A):
        for num in A:
            curr = self.root
            for i in range(31, -1, -1):
                curr_bit = (num >> i) & 1
                if curr.children[curr_bit] is None:
                    curr.children[curr_bit] = Node()
                curr = curr.children[curr_bit]

class Solution:
    def findMaximumXOR(self, nums):
        trie = Trie()
        trie.insert(nums)
        
        max_xor = 0
        
        for num in nums:
            curr = trie.root
            curr_sum = 0
            for i in range(31, -1, -1):
                required_bit = 1 - ((num >> i) & 1)  # If A[i] is 0, we need 1; if A[i] is 1, we need 0
                if curr.children[required_bit] is not None:
                    curr_sum |= (1 << i)  # Set the ith bit of curr result
                    curr = curr.children[required_bit]
                else:
                    curr = curr.children[1 - required_bit]
            max_xor = max(max_xor, curr_sum)  # Get max number
        
        return max_xor
