class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n)==1:
            return str(int(n)-1)
            
        candidates = set()
        prefix = n[:(len(n) + 1) // 2]
        prefix_number = int(prefix)
        
        for i in [-1, 0, 1]:
            new_prefix = str(prefix_number + i)
            if len(n) % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)
        
        candidates.add(str(10**(len(n)-1) - 1))
        candidates.add(str(10**len(n) + 1))
        
        
        candidates.discard(n)
        
      
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        return closest_palindrome

        