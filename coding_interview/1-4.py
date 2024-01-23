def is_palindrome(s: str) -> bool:
    """
    Given a string, write a function to check if it is a permutation of a
    palindrome. A palindrome is a word or phrase that is the same forwards and
    backwards. A permutation is a rearrangement of letters.
    """
    s = s.replace(" ", "")
    s = s.lower()
    for i in range(len(s) // 2):
        num = (len(s) - 1) - i
        if s[i] != s[num]:
            return False
    return True

def is_palindrome2(s):
    # 모든 알파벳 소문자로 변환
    s = s.lower()
    # 한 글자면
    if len(s) == 1:
        return True
    # 두 글자 이상이라면
    i = 0
    while i != len(s) // 2:
        if s[i] == s[i + (len(s) - 1) - (i * 2)]:
            i += 1
        else:
            return False
        return True

if __name__ == '__main__':
    # Write your test cases here
    assert is_palindrome("aba") == True
    assert is_palindrome("abc") == False
    assert is_palindrome("a") == True
    assert is_palindrome("Taco cat") == True
    assert is_palindrome("tac ocat") == True

    assert is_palindrome2("aba") == True
    assert is_palindrome2("abc") == False
    assert is_palindrome2("a") == True
    assert is_palindrome2("Taco cat") == True
    assert is_palindrome2("tac ocat") == True