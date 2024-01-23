# 정렬 사용 -> O(nlogn)
def is_permutation1(s1: str, s2: str) -> bool:
    """
    Given two strings, write a method to decide if one is a permutation of the
    other.
    """
    if len(s1) != len(s2):
        return False
    else:
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 == s2:
            return True
        else:
            return False

# 아스키 코드 사용 -> O(n)  
def is_permutation2(s1, s2):
    alphabet1 = [0] * 26
    alphabet2 = [0] * 26
    
    # s1
    for i in range(len(s1)):
        alphabet1[ord(s1[i]) - 97] += 1
    # s2
    for i in range(len(s2)):
        alphabet2[ord(s2[i]) - 97] += 1
    
    # 비교
    for i in range(len(s1)):
        if (alphabet1[i] != alphabet2[i]):
            return False
    return True

if __name__ == '__main__':
    # Write your test cases here
    
    assert is_permutation1("abcde", "abdec") == True
    assert is_permutation1("abcde", "abd") == False
    assert is_permutation1("abcde", "dsfav") == False
    assert is_permutation1("abcde", "abbcde") == False

    assert is_permutation2("abcde", "abdec") == True
    assert is_permutation2("abcde", "abd") == False
    assert is_permutation2("abcde", "dsfav") == False
    assert is_permutation2("abcde", "abbcde") == False