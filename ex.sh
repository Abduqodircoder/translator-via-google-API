#!/bin/bash
for i in {9000..9092}
do
echo "import googletrans

transator = googletrans.Translator()

# text = transator.translate(\"Hello world\",dest='uz')
txt = ''
with open(\"../english/eng${i-1}.txt\") as file:
    with open(\"uzbek${i-1}.txt\", 'a') as f:
        for line in file:
            txt = transator.translate(line, dest='uz').text + '\n'
            f.write(txt)
            print(f\"en:{line} uz:{transator.translate(line, dest='uz').text}\")
"> test${i}.py
done