def removeWhite(s, i=0, ):
    regex = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    if i == len(s):
        return ''
    elif s[i] in regex:
        return s[i] + removeWhite(s, i + 1)
    else:
        return removeWhite(s, i + 1)


def reverse(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse(s[:-1])


def is_palindrome(s: str) -> bool:
    s = removeWhite(s)
    half1 = s[:len(s) // 2]
    half2 = reverse(s[len(s) // 2:])
    if half1 == half2:
        return True
    elif half1 == half2[:-1]:
        return True
    return False


print(is_palindrome('mom'))
print(is_palindrome('madam i\'m adam'))
