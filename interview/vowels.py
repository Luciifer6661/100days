def vowelsCount(string1):
    vowels = ['a', 'e', 'i', 'o', 'u']

    lower1 = string1.lower()
    print(lower1)

    counter1 = {}
    counter2 = {}

    for ch in lower1:
        if ch in vowels:
            if ch in counter1:
                counter1[ch] += 1
            else:
                counter1[ch] = 1
        else:
            if ch in counter2:
                counter2[ch] += 1
            else:
                counter2[ch] = 1

    return counter1

string1 = 'Acomputerisamachine'
print(f"Vowels count followed by consonants:{vowelsCount(string1)}")


def vowelsCount(string1):
    vowels = ['a', 'e', 'i', 'o', 'u']

    counter1 = {}

    for ch in string1.lower():
        if ch in vowels:
            counter1[ch] = counter1.get(ch, 0) + 1

    return counter1

print(vowelsCount('Acomputerisamachine'))