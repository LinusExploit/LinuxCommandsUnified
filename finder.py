#!/usr/bin/python3
import re
import sys 

f = open('LinuxCommandsUnified.text','r')
all = f.read()

print("(+) Searching for the command {} (+)".format(sys.argv[1]))
print("(+)===========================================(+)")
print("")
print("")

search =  '\n\[ {} \].*?\n\[ .*? \]\n'.format(sys.argv[1])
result =  re.findall(search, all, re.DOTALL)
if result:
    print(result[0])
else:
    print('Nothing was found!')


