import string

al = [c for c in string.ascii_lowercase[::-1] if not c in ['i','o', 'l']]
ali = al.index
doubles = [c*2 for c in string.ascii_lowercase[::-1]]

def next_number(s):
    out = ''
    inc = True
    for c in s[::-1]:
        if inc: 
            v = al[al.index(c)-1]
            inc = v == 'a'
            out += v
        else:
            out += c
    return out[::-1]
    

def check(s):
    if not sum(1 for d in doubles if d in s) > 1:
        return False
    trip = zip(s, s[1:], s[2:])
    if any([ord(a) == ord(b)-1 == ord(c)-2 for a,b,c in trip]):
        return True
    return False

def next_pass(password):
    password = next_number(password)
    while not check(password):
        password = next_number(password)
    return password

if __name__ == "__main__":
    d = next_pass('vzbxkghb')
    print("part 1:", d)
    d = next_pass(d)
    print("part 2:", d)
