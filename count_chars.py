f = input("Type a sentence: ")

count_chars = {}
for char in f:
    if char not in count_chars:
        count_chars[char] = 0
    count_chars[char] += 1

for char in count_chars:
    print('The sentence has {} {}'.format(count_chars[char], char))
