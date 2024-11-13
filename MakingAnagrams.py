'''
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. 
In other words, both strings must contain the same exact letters in the same exact frequency. 
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme 
involving two large strings where encryption is dependent on the minimum number of character deletions required 
to make the two strings anagrams. Can you help her find this number?

Given two strings, s1 and s2, that may not be of the same length, determine the minimum number of character deletions required 
to make s1 and s2 anagrams. Any characters can be deleted from either of the strings.

Example.
s1 = abc
s2 = amnop

The only characters that match are the a's so we have to remove bc from s1 and mnop from s2 for a total of 6 deletions.

Function Description

Complete the makingAnagrams function in the editor below.

makingAnagrams has the following parameter(s):

string s1: a string
string s2: a string
Returns

int: the minimum number of deletions needed

Input Format

The first line contains a single string, s1.
The second line contains a single string, s2.

Constraints

1 <= |s1|, |s2| <= 10^4
It is guaranteed that s1 and s2 consist of lowercase English letters, ascii[a-z].
Sample Input

cde
abc
Sample Output

4
Explanation

Delete the following characters from our two strings to turn them into anagrams:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
4 characters have to be deleted to make both strings anagrams.
'''


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    freq1 = [0]*26
    freq2 = [0]*26
    
    for char in s1:
        freq1[ord(char) - ord('a')] += 1
    
    for char in s2:
        freq2[ord(char) - ord('a')] += 1
    
    deletions = 0
    for i in range(26):
        deletions += abs(freq1[i] - freq2[i])
        
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
