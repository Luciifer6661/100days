def find_duplicates(s2):
    words = s.split()
    seen = set()
    duplicates = set()

    for word in words:
        if word in seen:
            duplicates.add(word)
        else:
            seen.add(word)

    return list(duplicates)

s="This is a message from python interpretter. This message contains duplicate words. Message is important."
print(find_duplicates(s))