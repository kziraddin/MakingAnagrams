# Making Anagrams

## Problem Description

This program solves the "Making Anagrams" problem. Given two strings, it determines the minimum number of character deletions required to make the two strings anagrams of each other.

Two strings are considered anagrams if they contain the same characters with the same frequencies, regardless of order.

## Algorithm

The solution uses a frequency counting approach:

1. Create two frequency arrays (one for each string) to count occurrences of each lowercase letter.
2. Compare the frequency arrays and sum up the absolute differences.

This sum represents the total number of characters that need to be deleted to make the strings anagrams.

## Implementation

```python
def makingAnagrams(s1, s2):
    freq1 = *26
    freq2 = *26
    
    for char in s1:
        freq1[ord(char) - ord('a')] += 1
    
    for char in s2:
        freq2[ord(char) - ord('a')] += 1
    
    deletions = 0
    for i in range(26):
        deletions += abs(freq1[i] - freq2[i])
        
    return deletions
