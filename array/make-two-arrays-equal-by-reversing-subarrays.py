class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for item in target:
            if item not in arr:
                return False
            arr.remove(item)
        return True