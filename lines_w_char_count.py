#!/usr/bin/python

num_lines = 0
num_words = 0
num_chars = 0

with open ('dns', 'r') as f:
        for line in f:
                words = line.split()

                num_lines +=1
                num_words +=len(words)
                num_chars +=len(line)

        print "Number of lines: %s, number of words: %s, number of characters: %s " % (num_lines, num_words, num_chars)
~
