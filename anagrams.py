from collections import Counter


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for ch in s1:

        if ch in freq1:
            # if character has already been counted in freq1, increment it by 1 if found again
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in freq2:
            # if character has already been counted in freq2, increment it by 1 if found again
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
        return True


# builds a table of occurrences by just passing the string as an argument.
# Compare dictionaries with an comparative operator
def simple_are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)


# using sorted method (e.g "nameless" sorted is "aeelmnss" and "salesmen" sorted is "aeelmnss"
def sorted_are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
