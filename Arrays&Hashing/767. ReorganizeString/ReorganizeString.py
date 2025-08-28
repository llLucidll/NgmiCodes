from collections import Counter
def reorganizeString(s: str) -> str:
    
    string_length = len(s)
    char_count = Counter(s)
    max_freq = max(char_count.values())

    if max_freq > (string_length + 1) // 2:
        return ""

    index = 0

    reorganized = [None] * string_length

    for char, freq in char_count.most_common():
        while freq:
            reorganized[index] = char
            index += 2
            freq -= 1
            # If we go past the string length, start filling the odd indices
            if index >= string_length:
                index = 1
    
    return ''.join(reorganized)
                

