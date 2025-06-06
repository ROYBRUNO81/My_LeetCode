def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    left_index = n
    right_index = 0

    for i in range(n-1, 0, -1):
        if nums[i-1] < nums[i]:
            left_index = i-1
            break
    if left_index == n:
        return nums.reverse()
    else:
        for i in range(n-1, -1, -1):
            if nums[left_index] < nums[i]:
                temp =  nums[left_index]
                nums[left_index] = nums[i]
                nums[i] = temp
                break
        sub_nums = nums[left_index + 1:].reverse()
        return nums[:left_index + 1].append(sub_nums)