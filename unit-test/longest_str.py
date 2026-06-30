def find_longest_string(strings: list[str]) -> str | None:
    if not strings:
        return None
    
    longest_string = ""
    for s in strings:
        if not isinstance(s, str):
            raise TypeError("All elements in the list must be string")
        if len(s) > len(longest_string):
            longest_string = s

    return longest_string