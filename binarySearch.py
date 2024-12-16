'''Binary search O(log2n)'''
def binary_search(sequence, item):
    begin_point = 0
    end_point = len(sequence) - 1
    while begin_point <= end_point:
        midpoint = begin_point + (begin_point + end_point) // 2
        midpoint_value = sequence[midpoint]
        if item == midpoint_value:
            return midpoint
        elif item < midpoint:
            end_index = midpoint - 1
        else:
            start_point = midpoint + 1
    return None

'''35. Search Insertion Position'''
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
nums_a = [1,3,5,6]
target_a = 5
print(searchInsert(nums_a, target_a))