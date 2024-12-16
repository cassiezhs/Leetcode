'''485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's in the array.
time complexity: O(n)
'''
def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_count = max_count = 0
        for i in nums:
                if i == 1:
                        current_count += 1
                else:
                        max_count = max(max_count, current_count)        
                        current_count = 0
        return max(max_count, current_count)       
nums = [1,1,0,1,1,1]       
print(findMaxConsecutiveOnes(nums))       

'''
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
'''
class Solution(object):
   def moveZeroes(self, nums):
      """
      :type nums: List[int]
      :rtype: None Do not return anything, modify nums in-place instead.
      """
      insert_index = 0
      for i in range(len(nums)):
         if nums[i] != 0:
            nums[insert_index]=nums[i]
            insert_index+=1
      for i in range(insert_index,len(nums)):
         nums[i]=0
nums = [0,1,5,0,3,8,0,0,9]
ob1 = Solution()
ob1.moveZeroes(nums)
print(nums)           


                    
                        