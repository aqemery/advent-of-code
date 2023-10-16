find_row = 2947
find_col = 3029

count = 0
size = 1
code = 20151125

while True:
    size += 1
    for col in range(size):
        count += 1
        code = (code * 252533) % 33554393
        if find_row == size - col and find_col == col+1:
            print(code)
            exit()