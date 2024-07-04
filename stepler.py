
#https://github.com/platta349/dz0207

text1 = str(input())
text2 = str(input())
symbols = ".,!?:;'\"-—"
for symbol in symbols:
    text1 = text1.replace(symbol, '')
    text2 = text2.replace(symbol, '')
text1 = text1.lower()
text2 = text2.lower()

text1 = text1.split()
text2 = text2.split()

uniqaln_slova1 = set(text1)
uniqaln_slova2 = set(text2)


print("Уникальные слова в первом тексте:", uniqaln_slova1.difference(uniqaln_slova2))
print("Уникальные слова во втором тексте:", uniqaln_slova2.difference(uniqaln_slova1))

edenstv_slova1 = set(text1)
edenstv_slova2 = set(text2)
print("Слова, повторяющиеся один раз за весь первый текст", edenstv_slova1)
print("Слова, повторяющиеся один раз за весь второй текст", edenstv_slova2)

obschie_slova = edenstv_slova1.intersection(edenstv_slova2)
print("Общие слова:", obschie_slova)

ednstvennoe = uniqaln_slova1.symmetric_difference(uniqaln_slova2)
print(f"Слова, которые присутствуют только в одном из текстов:", ednstvennoe)