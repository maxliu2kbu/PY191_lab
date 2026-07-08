import re

counter = {}
sentence = "It was the best of times, it was the worst of times... the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."
for i in sorted(re.split(r"\W+",sentence)):
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
del counter[""]
# print(counter)

words = sentence.split()
count = 0
new = []
for i in words:
    if count % 2 == 1:
        new.append(i[::-1])
    else:
        new.append(i)
    count += 1
builder = ""
for j in new:
    builder += j + ' '
print(builder)

string = "Happy Birthday to Jace"
builder = ""
count = 0
for i in string:
    count += 1
    if (count % 7 == 0):
        builder += str(7)
    else:
        builder += i
print(builder)