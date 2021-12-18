fft = input()
offset = int(fft[:7])
fft = list(map(int, list(fft))) * 10000
fft = fft[offset:]

for loop in range(100):
    for i in range(len(fft) - 1, 0, -1):
        fft[i - 1] = int(str(fft[i - 1] + fft[i])[-1:])
print("".join(map(str, fft[:8])))
