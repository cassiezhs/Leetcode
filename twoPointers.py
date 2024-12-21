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

'''75. Sort Colors
Time complexity#: O(n)
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        colors = nums
        start = 0
        curr = 0
        end = len(colors) - 1
        while curr <= end:
            if colors[curr] == 0:
                colors[curr], colors[start] = colors[start], colors[curr]
                start += 1
                curr += 1
            elif colors[curr] == 1:
                curr += 1
            else:
                colors[curr], colors[end] = colors[end], colors[curr]                    
                end -= 1
        return colors

'''151. Reverse Words in a String'''


'''557. Reverse Words in a String III'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l = 0

        for r in range(len(s)):
            if s[r] == " " or s[r] == len(s) - 1:
                temp_l, temp_r = l, r-1

                if r == len(s) - 1:
                    temp_r = r
                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l += 1
                    temp_r -= 1
                l = r + 1
        return "".join(s)
'''408. Valid Word Abbreviation'''
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        word_ptr = 0
        abbr_ptr = 0
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            if abbr[abbr_ptr].isdigit():
                steps = 0

                if abbr[abbr_ptr] == "0":
                    return False
                
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    steps = steps * 10 + int(abbr[abbr_ptr])

                    abbr_ptr += 1
                word_ptr += steps
            else:
                    if word[word_ptr] != abbr[abbr_ptr]:
                        return False
                    word_ptr += 1
                    abbr_ptr += 1
        return word_ptr == len(word) and abbr_ptr == len(abbr)
    
'''246. Strobogrammatic Number'''
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # Define valid strobogrammatic pairs
        strobogrammatic_pairs = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        l, r = 0, len(num) - 1
        while l <= r:
            # Check if the characters are valid strobogrammatic pairs
            if num[l] not in strobogrammatic_pairs or strobogrammatic_pairs[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True
num = "2"
ob1 = Solution()
ob1.isStrobogrammatic(num)         
