## Leetcode probelm link:
## https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        s = set()
        for n in arr:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
        
        for k, v in dict.items():
            s.add(v)
            
        if len(dict) == len(s):
            return True
        else:
            return False
