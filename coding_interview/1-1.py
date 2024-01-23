# 딕셔너리 자료구조를 사용해서 해결 -> O(n)
def is_unique_characters(s: str) -> bool:
    """
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
    """
    s = s.lower()
    dic = {}
    for i in range(len(s)):
        # 이미 딕셔너리에 문자가 존재함
        if s[i] in dic:
            return False
        else:
            dic[s[i]] = 1
    return True

# 이중 for문으로 해결 -> O(n^2)
def is_unique_characters2(s: str) -> bool:
    s = s.lower()
    for i in range(len(s)):
        n = s[i]
        for j in range(i + 1, len(s)):
            if n == s[j]:
                return False
    return True

# 정렬을 이용해서 해결 -> O(nlogn)
def is_unique_characters3(s: str) -> bool:
    s = s.lower()
    s = sorted(s) # quick sort
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

if __name__ == '__main__':
    # Write your test cases here
    testcase1 = "abcde"  # True
    testcase2 = "aabbcc" # False
    testcase3 = "AaBbc"  # False
    testcase4 = "zxyut"  # True
    testcase5 = "abcabc"  # False

    assert is_unique_characters(testcase1) == True
    assert is_unique_characters(testcase2) == False
    assert is_unique_characters(testcase3) == False
    assert is_unique_characters(testcase4) == True
    assert is_unique_characters(testcase5) == False

    assert is_unique_characters2(testcase1) == True
    assert is_unique_characters2(testcase2) == False
    assert is_unique_characters2(testcase3) == False
    assert is_unique_characters2(testcase4) == True
    assert is_unique_characters2(testcase5) == False

    assert is_unique_characters3(testcase1) == True
    assert is_unique_characters3(testcase2) == False
    assert is_unique_characters3(testcase3) == False
    assert is_unique_characters3(testcase4) == True
    assert is_unique_characters3(testcase5) == False