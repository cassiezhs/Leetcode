"""
NO.187 Repeated DNA Sequences
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        to_int = {"A": 0, "C": 1, "G": 2, "T": 3}
        encoded_sequence = [to_int[c] for c in s]
        k = 10
        n = len(s)
        #if the length of the test case is <= 10
        if n <= k:
            return []
        
        a = 4 #base-4 encoding
        h = 0 #hash value

        seen_hashes, output = set(), set()  # Sets to track hashes and repeated sequences

        a_k = 1 # Stores a^L for efficient rolling hash updates

        ## Sliding window approach to update the hash efficiently
        for start in range(1, n-k+1):
            # Remove the leftmost character and add the new rightmost character
            h = h*a-encoded_sequence[start-1] * a_k -encoded_sequence[start+k-1]
        # If this hash has been seen_hashes before, add the corresponding substring to the output
        if h in seen_hashes:
            output.add(s[start : start + k])
        else:
            seen_hashes.add(h)
        return list(output)  # Convert set to list before returning
    

