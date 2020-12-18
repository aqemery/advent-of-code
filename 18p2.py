import sys
import re

out = 0

for line in sys.stdin.readlines():
  line = line.strip().replace(' ','')

  while '(' in line or '+' in line:
    while m := re.search('\d+(\+\d+)+', line):
      s = m.group()
      line = line.replace(s,str(eval(s)))

    while m := re.search('\(\d+(\*\d+)+\)', line):
      s = m.group()
      line = line.replace(s,str(eval(s)))

    while m := re.search('\(\d*\)', line):
      s = m.group()
      line = line.replace(s,str(eval(s)))
  
  out += eval(line)
print(out )