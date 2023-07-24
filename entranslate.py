import googletrans

transator = googletrans.Translator()

# text = transator.translate("Hello world",dest='uz')
txt = ''
tmp = ''
i = 0
with open("../english/ennw.txt") as file:
    for line in file:
        if i > 2790:
            txt = transator.translate(line, dest='uz').text + '\n'
            tmp += txt
        if i % 10 == 0 and i > 2790:
            with open("../english/uznw.txt", 'a') as f:
                f.write(tmp)
                print(f"en:{i} uz:{tmp}")
                tmp = ''
        i += 1
