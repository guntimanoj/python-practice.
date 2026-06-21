def find_max(nums):
    if not nums:
        raise ValueError("Cannot find max of empty array")
    largest = nums[0]
    for n in nums[1:]:
        if n > largest:
            largest = n
    return largest


if __name__ == "__main__":
    print(find_max([3, 7, 2, 9, 4]))    
    print(find_max([-5, -1, -10]))        
    print(find_max([42]))                 