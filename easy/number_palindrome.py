#Given an integer x, return true if x is a palindrome, and false otherwise.
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

def isPalindrome(x):
    string_number = str(x)

    reverse_srt = string_number[::-1]
    if reverse_srt == string_number:
        return True
    else:
        return False


num = 1234
print(isPalindrome(num))