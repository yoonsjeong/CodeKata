string = "babad"


def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[-(i+1)]:
            return False
    return True


def longest_palindrome_naive(s: str):
    longest = ""
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            test = s[i:j+1]
            if is_palindrome(test) and len(test) > len(longest):
                longest = test
    return longest


# out = longest_palindrome_naive("i had a xanax")
# print(out)

def expand_from_mid(s, left, right):
    if not 0 <= left <= right < len(s): return ""

    while 0 <= left <= right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]


def longest_palindrome_n2(s: str):
    n = len(s)
    longest = ""
    for i in range(n):
        str1 = expand_from_mid(s, i, i)
        str2 = expand_from_mid(s, i, i+1)
        if len(str1) > len(longest): longest = str1
        if len(str2) > len(longest): longest = str2
    return longest

out = longest_palindrome_n2("helloracecarexistsxxannaxx")
print(out)