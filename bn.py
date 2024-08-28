from collections import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        products = []

        for num in spells:
            prod = [num * i for i in potions]
            products.append(prod)
        ans = []
        
        for array in products:
            left, right = 0, len(array)
            n = len(array)
            
            while left <= right:
                mid = (left + right)//2

                if array[mid] >= success:
                    right = mid
                else:
                    left = mid + 1
            ans.append((n - mid) + 1)

        return ans
        

print(Solution.successfulPairs([5,1,3],[1,2,3,4,5]))