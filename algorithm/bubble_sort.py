from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    """
    Sort a list using the bubble sort algorithm.
    """
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                # swap
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    return nums

if __name__ == '__main__':
    # Write your test cases here   
    testcase1 = [5, 4, 3, 2, 1]
    testcase2 = [100, 0, -12, 9, 1]

    assert bubble_sort(testcase1) == [1, 2, 3, 4, 5]
    assert bubble_sort(testcase2) == [-12, 0, 1, 9, 100]
