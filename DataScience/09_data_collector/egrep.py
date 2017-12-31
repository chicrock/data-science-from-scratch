# _*_ coding: utf-8 _*_
import sys, re

regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)