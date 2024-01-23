from typing import List

# 오른쪽으로 90도 회전
def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Given an image represented by an NxN matrix, where each pixel in the image
    is 4 bytes, write a method to rotate the image by 90 degrees. Can you do
    this in place?
    """
    n = len(matrix)
    rotated_matrix = [] # [] => [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    for i in range(n):
        row_list = []
        for j in range(n):
            row_list.append(0)
        rotated_matrix.append(row_list)
    
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j] 
            # rotated_matrix[i][j] = matrix[j][n - 1 - i]
            
    return rotated_matrix

# 오른쪽으로 180도 회전
def right_180_rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rotated_matrix = []
    n = len(matrix)

    for i in range(n):
        row_list = []
        for j in range(n):
            row_list.append(0)
        rotated_matrix.append(row_list)

    for i in range(n):
        for j in range(n):
            rotated_matrix[n - 1 - i][n - 1 - j] = matrix[i][j]

    return rotated_matrix

# 오른쪽으로 270도 회전
def right_270_rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rotated_matrix = []
    n = len(matrix)
    for i in range(n):
        row_list = []
        for j in range(n):
            row_list.append(0)
        rotated_matrix.append(row_list)

    for i in range(n):
        for j in range(n):
            rotated_matrix[n - 1 - j][i] = matrix[i][j]

    return rotated_matrix

# 왼쪽으로 90도 회전
def left_90_rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rotated_matrix = []
    n = len(matrix) # rotated_matirx의 행의 크기
    # 0으로 초기화
    for i in range(n):
        row_list = []
        for j in range(n):
            row_list.append(0)
        rotated_matrix.append(row_list)

    # 회전
    for i in range(n):
        for j in range(n):
            rotated_matrix[n - 1 - j][i] = matrix[i][j]

    return rotated_matrix


# 왼쪽으로 180도 회전
def left_180_rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rotated_matrix = []
    n = len(matrix) 
    for i in range(n):
        row_list = []
        for j in range(n):
            row_list.append(0)
        rotated_matrix.append(row_list)

    for i in range(n):
        for j in range(n):
            rotated_matrix[n - 1 - i][n - 1 - j] = matrix[i][j]

    return rotated_matrix

# 왼쪽으로 270도 회전
def left_270_rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rotated_matrix = []
    n = len(matrix)
    for i in range(n):
        row_list = []
        for j in range(n):
            row_list.append(0)
        rotated_matrix.append(row_list)

    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]

    return rotated_matrix

if __name__ == '__main__':
    # Write your test cases here
    testcase1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert rotate_matrix(testcase1) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert right_180_rotate_matrix(testcase1) == [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    assert right_270_rotate_matrix(testcase1) == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    assert left_90_rotate_matrix(testcase1) == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    assert left_180_rotate_matrix(testcase1) == [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    assert left_270_rotate_matrix(testcase1) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]