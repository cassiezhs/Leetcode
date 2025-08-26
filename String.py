"""
58. Length of Last Word
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        ptr = len(s) - 1
        count = 0
        
        # skip trailing spaces
        while ptr >= 0 and s[ptr] == ' ':
            ptr -= 1
        
        # count characters of the last word
        while ptr >= 0 and s[ptr] != ' ':
            count += 1
            ptr -= 1
        
        return count
