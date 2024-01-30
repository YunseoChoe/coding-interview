def is_one_away(s1: str, s2: str) -> bool:
    """
    There are three types of edits that can be performed on strings: insert a
    character, remove a character, or replace a character. Given two strings,
    write a function to check if they are one edit (or zero edits) away.
    """
    # s1 == s2
    if s1 == s2:
        return True
    # 대체
    elif len(s1) == len(s2):
        return replace(s1, s2)
    # 삭제
    elif len(s1) - len(s2) == 1:
        return remove(s1, s2)
    # 삽입
    elif len(s1) - len(s2) == -1:
        return remove(s2, s1)
    # 길이 차이가 2이상
    else:
        return False

def replace(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1

    if cnt == 1:
        return True
    else:
        return False

def remove(s1, s2):
    s1_index = 0
    s2_index = 0
    while s1_index < len(s1) and s2_index < len(s2):
        if s1[s1_index] == s2[s2_index]:
            s1_index += 1
            s2_index += 1
        # s1[s1_index] != s2[s2_index]
        else:
            if s1_index != s2_index:
                return False
            s1_index += 1
    return True

# def remove(s1, s2):
#     s1_index = 0
#     s2_index = 0
#     cnt = 0
#     while s1_index < len(s1) and s2_index < len(s2):
#         # s1[s1_index] == s2[s2_index] 
#         if s1[s1_index] == s2[s2_index]:
#             s1_index += 1
#             s2_index += 1
#         # s1[s1_index] != s2[s2_index] 
#         else:
#             s1_index += 1
#             cnt += 1
    
#     if cnt == 0 or cnt == 1:
#         return True
#     else:
#         return False

if __name__ == '__main__':
    # Write your test cases here
    testcase1 = "abc"
    assert is_one_away(testcase1, "abd") == True
    assert is_one_away(testcase1, "ab") == True
    assert is_one_away(testcase1, "abcd") == True
    assert is_one_away(testcase1, "a") == False
    assert is_one_away(testcase1, "abcde") == False
    assert is_one_away(testcase1, "abc") == True
    assert is_one_away(testcase1, "ab") == True
