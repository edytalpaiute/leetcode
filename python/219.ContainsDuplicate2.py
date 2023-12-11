class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
       control = []
       
       if len(nums) == 0 or len(nums) == 1:
           return False
       for i in range(len(nums)):
           if nums.count(nums[i]) > 0 and nums[i]!= None:
               copy = nums[i]
               nums[i] = None
               try:
                index2 = nums.index(copy)
                control.append(abs(i-index2))
               except Exception:
                  pass
       for i in range(len(control)):
          if control[i] > k:
             return False
       return True
      
           

sol = Solution()                #  0 1 2 3 4 5
print(sol.containsNearbyDuplicate([1,2,3,1,2,3],2))