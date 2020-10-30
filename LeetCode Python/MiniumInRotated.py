def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left_point = 0
    right = len(nums) - 1

    if nums[right] > nums[0]:
        return nums[0] #no rotation, already sorted so return smallest number

    while right >= left_point:
        mid = (right + left_point) // 2
        if right == left_point:
            return nums[0]

        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        if nums[mid] > nums[0]:
            left = mid + 1
        else:
            right = mid - 1


    
    # x = min(nums)
    # return x
        
    
print(findMin([3,4,5,1,2]))
        