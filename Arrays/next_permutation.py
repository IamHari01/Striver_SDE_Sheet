def nextPermutation(nums):
    # Find the first decreasing element from the right
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
        
    if i >= 0:
        # Find the element just larger than nums[i] to swap with
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        
    # Reverse the suffix starting at i + 1
    left = i + 1
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        
    return nums

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3],
        [3, 2, 1],
        [1, 1, 5],
        [1, 3, 2]
    ]
    for tc in test_cases:
        tc_copy = tc.copy()
        result = nextPermutation(tc_copy)
        print(f"Next permutation of {tc} -> {result}")
