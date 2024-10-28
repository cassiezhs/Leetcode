'''Binary search O(log2n)'''
def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start_point = 0
        end_point = len(nums) - 1
        while start_point <= end_point:
            midpoint = start_point + (end_point - start_point) // 2
            midpoint_value = nums[midpoint]
            if target == midpoint_value:
                return midpoint
            elif target < midpoint_value:
                end_point = midpoint - 1
            else:
                start_point = midpoint + 1
        # If the target is not found, start_point will be the insert position
        return start_point