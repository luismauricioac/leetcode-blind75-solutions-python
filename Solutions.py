import re


def is_palindrome(input: str) -> bool:
    str_cleaned = re.sub(r"[^a-zA-Z0-9]", "", input)
    last = len(str_cleaned) - 1
    for index, item in enumerate(str_cleaned):
        if (item != str_cleaned[last]):
            return False
        last -= 1
    return True
