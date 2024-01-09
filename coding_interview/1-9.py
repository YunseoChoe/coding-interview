def is_rotation(s1: str, s2: str) -> bool:
    """
    Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, s1 and s2, write code to check if s2 is a
    rotation of s1 using only one call to isSubstring
    """
    # s1을 배열로 바꾸기
    s1_array = []
    for i in range(len(s1)):
        s1_array.append(s1[i])

    cnt = 0
    for i in range(len(s2)):
        if s2[i] in s1_array:
            cnt += 1
            print(cnt)
        else:
            cnt = 0
            print(cnt)

    if cnt == len(s2):
        return True
    else:
        return False

if __name__ == '__main__':
    # Write your test cases here
    testcase1_1 = "ppledea"
    testcase1_2 = "apple"
    testcase2_1 = "english"
    testcase2_2 = "hsli"
    testcase3_1 = "macbook"
    testcase3_2 = "koobcam"
    testcase4_1 = "hello"
    testcase4_2 = "ell"
    testcase5_2 = "ol"

    assert is_rotation(testcase1_1, testcase1_2) == True
    assert is_rotation(testcase2_1, testcase2_2) == False
    assert is_rotation(testcase3_1, testcase3_2) == False
    assert is_rotation(testcase4_1, testcase4_2) == True
    assert is_rotation(testcase4_1, testcase5_2) == False