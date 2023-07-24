with open("../english/en.txt") as f :
    lines = f.readlines()
    s = set(lines)
with open("../english/ennw.txt",'a') as f2:
    for line in s:
        f2.write(line)