with open("../english/english.txt") as f:
    lines = f.readlines()
    for ind, line in enumerate(lines):
        if line == '.\n' or line == '\n':  # if line contains a match
            lines[ind] = ""  # set line to empty string
    with open("../english/english.txt", "w") as f:  # reopen with w to overwrite
        f.writelines(lines)  # write updated lines
