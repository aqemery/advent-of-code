import sys

lines = sys.stdin.readlines()
byte_len = len(lines[0])-1

def to_int(x):
  return int(''.join(x),2)

def consider(lines, index, val):
  return [l for l in lines if l[index] == val]

def common(lines, index):
  half = len(lines) / 2
  if [l[index] for l in lines].count('1') >= half:
    return '1'
  return '0'

def uncommon(lines, index):
  return '1' if common(lines,index) == '0' else '0'

oxygen = lines
for i in range(byte_len):
  oxygen = consider(oxygen, i, common(oxygen, i))
  if len(oxygen) == 1:
    break

oxygen_value = to_int(oxygen[0])

co2 = lines
for i in range(byte_len):
  co2 = consider(co2, i, uncommon(co2, i))
  if len(co2) == 1:
    break

co2_value = to_int(co2[0])

print(oxygen_value * co2_value)
