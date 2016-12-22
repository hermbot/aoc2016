'''--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately, your signal
is only partially jammed, and protocol in situations like this is to switch
to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the
repeating message signal (your puzzle input), but the data seems quite
corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each
position. For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
The most common character in the first column is e; in the second, a; in the
third, s, and so on. Combining these characters returns the error-corrected
message, easter.

Given the recording in your puzzle input, what is the error-corrected version
of the message being sent?'''

import collections

f = open('input6.txt', 'r')
data = f.readlines()

# Woo list comprehension
data = [i.strip() for i in data]

char0 = []
char1 = []
char2 = []
char3 = []
char4 = []
char5 = []
char6 = []
char7 = []

for i in data:
    char0.append(i[0])
    char1.append(i[1])
    char2.append(i[2])
    char3.append(i[3])
    char4.append(i[4])
    char5.append(i[5])
    char6.append(i[6])
    char7.append(i[7])


print(collections.Counter(char0).most_common(1)[0])
print(collections.Counter(char1).most_common(1)[0])
print(collections.Counter(char2).most_common(1)[0])
print(collections.Counter(char3).most_common(1)[0])
print(collections.Counter(char4).most_common(1)[0])
print(collections.Counter(char5).most_common(1)[0])
print(collections.Counter(char6).most_common(1)[0])
print(collections.Counter(char7).most_common(1)[0])