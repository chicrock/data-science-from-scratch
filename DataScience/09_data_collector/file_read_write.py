# _*_ coding: utf-8 _*_

#file_for_reading = open('File.txt', 'r')
#file_for_writing = open('write_File.txt', 'w')
#file_for_appending = open('appending_file.txt', 'a')
#file_for_writing.close()

import re

start_with_hash = 0
with open('File.txt', 'r') as f:
    for line in f:
        if re.match("^#", line):
            start_with_hash += 1

print start_with_hash