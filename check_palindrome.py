def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(is_palindrome("racecar"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("hello"))