def urlify(s: str, length: int) -> str:
    """
    Write a method to replace all spaces in a string with '%20'. You may assume
    that the string has sufficient space at the end to hold the additional
    characters, and that you are given the "true" length of the string.
    """
    # 문자열 -> 하나의 배열로 만들기
    charArray = []
    for i in range(len(s)):
        charArray.append(s[i])
    # 문자열 -> 리스트
    for i in range(len(charArray)):
        if charArray[i] == ' ':
            charArray[i] = '%20'
    # 리스트 -> 문자열
    charArray = ''.join(charArray)
    
    return charArray

def urlify2(s, length):
    # 문자열 -> list
    s = list(s)
    for i in range(len(s)):
        if s[i] == " ":
            s[i] = "%20"
    # list -> 문자열
    for i in range(len(s)):
        s = ''.join(s)
    return s

if __name__ == '__main__':
    # Write your test cases here
    testcase1 = "abc "          # 'abc%20'
    testcase2 = " ffdvs ds "    # '%20%20ffdvs%20ds%20'
    testcase3 = "Mr John Smith"

    assert urlify(testcase1, len(testcase1)) == "abc%20"
    assert urlify(testcase2, len(testcase2)) == "%20ffdvs%20ds%20"
    assert urlify(testcase3, len(testcase3)) == "Mr%20John%20Smith"
    assert urlify2(testcase3, len(testcase3)) == "Mr%20John%20Smith"