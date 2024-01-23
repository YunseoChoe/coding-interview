from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    """
    Selection sort on a list.
    """
    # 최솟값 찾기
    for i in range(len(nums)):
        min_index = i
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                min_index = j
        # swap
        temp = nums[i] 
        nums[i] = nums[min_index]
        nums[min_index] = temp     

    return nums
if __name__ == '__main__':
    # Write your test cases here
    testcode1 = [5, 4, 3, 2, 1]
    assert selection_sort(testcode1) == [1, 2, 3, 4, 5]