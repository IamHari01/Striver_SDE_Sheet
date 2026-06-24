def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
            
    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {nums}")
    print(f"Maximum subarray sum: {maxSubArray(nums)}")
