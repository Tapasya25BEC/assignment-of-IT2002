# C12: Palindrome check using a deque

from collections import deque

def is_palindrome(s):
    d = deque(c.lower() for c in s if c.isalnum())
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("hello"))
print(is_palindrome(""), is_palindrome("a"))
