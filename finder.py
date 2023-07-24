# text = transator.translate("Hello world",dest='uz')
txt = ''
tmp = ''
i = 1
with open("../english/uzbek.txt") as file:
    for line in file:
        if line == '.\n' or line == '\n':
            print(f"{i} : {line}")
        i += 1
