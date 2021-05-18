import re
import sys 

f = open('LinuxCommandsUnified.text','r')
all = f.read()

search =  '\[ {} \].*?\[.*?\]'.format(sys.argv[1])
result =  re.findall(search, all, re.DOTALL)
print(result[0])



