import re
'''time complexity is 
O(n)
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r"[^a-z0-9]","",s.lower())
        l = 0
        r = len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
s = "A man, a plan, a canal: Panama"
ob1 = Solution()
ob1.isPalindrome(s)
print(ob1)           

'''3Sum
 sorting the array takes O(nlog(n)) + the nested loop takes  O(n^2)
'''
def find_sum_of_three(nums, target):
    nums.sort()

    for i in range(0, len(nums)-2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            if triplet == target:
                return True
                
            elif triplet < target:
                low += 1
            
            else:
                high -= 1
    
    return False