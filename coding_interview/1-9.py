def is_rotation(s1: str, s2: str) -> bool:
    """
    Assume you have a method isSubstring which checks if one word is a substring
    of another. Given two strings, s1 and s2, write code to check if s2 is a
    rotation of s1 using only one call to isSubstring
    """
    # 1. 문자열 s1을 딕셔너리로 저장
    s1_dict = {}
    for i in range(len(s1)):
        s1_dict[i] = s1[i]

    # 2. 문자열 s2를 딕셔너리로 저장 (s1_dict에 맞게)
    s2_dict = {}

    for i in range(len(s2)):
        cnt = 1
        for j in range(len(s1)):
            if s2[i] == s1[j] and cnt != len(s2):
                cnt += 1
                s2_dict[j] = s2[i]

    # 3. s2_dict의 key들이 회전 방향대로 잘 배치 되었는지 확인
    key_list = []
    for key in s2_dict:
        key_list.append(key)

    cnt = 0
    for i in range(len(key_list) - 1):
        if key_list[i] == len(s1) - 1:
            cnt += 1
        elif key_list[i] != len(s1) - 1 and key_list[i] <= key_list[i + 1]:
            cnt += 1
        else:
            cnt += 0

    if cnt == len(key_list) - 1:
        return True
    else:
        return False

if __name__ == '__main__':
    
    testcase1_1 = "hello"
    testcase1_2 = "oh"
    testcase1_3 = "le"
    testcase1_4 = "hl"
    testcase2_1 = "macbook"
    testcase2_2 = "ookm"
    testcase2_3 = "koobcam"

    assert is_rotation(testcase1_1, testcase1_2) == True
    assert is_rotation(testcase1_1, testcase1_3) == False
    assert is_rotation(testcase1_1, testcase1_4) == True
    assert is_rotation(testcase2_1, testcase2_2) == True
    assert is_rotation(testcase2_1, testcase2_3) == False

