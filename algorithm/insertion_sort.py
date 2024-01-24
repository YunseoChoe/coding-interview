from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    """
    Sort a list using the insertion sort algorithm.
    """
    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[j] > nums[j + 1]:
                # swap
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    return nums

if __name__ == '__main__':
    # Write your test cases here
    testcase1 = [5, 4, 3, 2, 1]
    testcase2 = [0, -9, 100, 1, 80]

    assert insertion_sort(testcase1) == [1, 2, 3, 4, 5]
    assert insertion_sort(testcase2) == [-9, 0, 1, 80, 100]