'''Of course, that would be the message - if you hadn't agreed to use a
modified repetition code instead.

In this modified code, the sender instead transmits what looks like
random data, but for each character, the character they actually want to
send is slightly less likely than the others. Even after signal-jamming
noise, you can look at the letter distributions in each column and choose
the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a;
in the second, d, and so on. Repeating this process for the remaining
characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology,
what is the original message that Santa is trying to send?'''

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


print(collections.Counter(char0).most_common()[-1])
print(collections.Counter(char1).most_common()[-1])
print(collections.Counter(char2).most_common()[-1])
print(collections.Counter(char3).most_common()[-1])
print(collections.Counter(char4).most_common()[-1])
print(collections.Counter(char5).most_common()[-1])
print(collections.Counter(char6).most_common()[-1])
print(collections.Counter(char7).most_common()[-1])