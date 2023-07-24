import googletrans

transator = googletrans.Translator()

# text = transator.translate("Hello world",dest='uz')
txt = ''
tmp = ''
i = 0
with open("../english/english.txt") as file:
    for line in file:
        if i > -1:
            txt = transator.translate(line, dest='uz').text + '\n'
            tmp += txt
        if i % 10 == 0 and i > -1:
            with open("../english/uzbek_2.txt", 'a') as f:
                f.write(tmp)
                print(f"en:{i} uz:{tmp}")
                tmp = ''
        i += 1
