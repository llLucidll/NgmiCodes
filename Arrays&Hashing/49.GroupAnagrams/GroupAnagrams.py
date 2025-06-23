def groupAnagrams(strs):
    words = {}

    for word in strs:
        word_s = sorted(word) # This function returns a list of sorted chars
        word_s = "".join(word_s) # Turns it into a joined string
        if word_s in words:
            words[word_s].append(word)
        else:
            words[word_s] = [word]
    
    result = list(words.values())