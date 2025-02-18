# def fred():
#    print("Zap")
#
# def jane():
#    print("ABC")
#
# jane()
# fred()
# jane()


# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Blastoff!')

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# how to count a line in a textfiles
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('X-DSPAM-Confidence:'):
#         count = count + 1
# print('There were', count, 'X-DSPAM-Confidence lines in', fname)

# fhand = open('mbox-short.txt')

# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     words = line.split()
#     print(words )

# Search for lines that start with 'From'
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
