def czy_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Test
print(czy_anagram("listen", "silent"))
print(czy_anagram("hello", "world"))
