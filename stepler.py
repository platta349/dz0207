text1 = "Питон — мощный язык программирования. Он широко используется в науке о данных."
text2 = "Питон хорош для анализа данных. Он также используется в веб-разработке."
symbols = ".,!?:;'\"-—"
for symbol in symbols:
    text1 = text1.replace(symbol, '')
    text2 = text2.replace(symbol, '')
text1 = text1.lower()
text2 = text2.lower()

uniqaln_slova1 = set()
uniqaln_slova2 = set()
print("Уникальные слова в первом тексте:", uniqaln_slova1.difference(uniqaln_slova2))
print("Уникальные слова во втором тексте:", uniqaln_slova2.difference(uniqaln_slova1))


edenstv_slova1 = set()
edenstv_slova2 = set()
print("Слова, повторяющиеся один раз за весь текст", edenstv_slova1)
print("Слова, повторяющиеся один раз за весь текст", edenstv_slova2)

obschie_slova = edenstv_slova1.intersection(edenstv_slova2)
print("Общие слова:", obschie_slova)


ednstvennoe = uniqaln_slova1.symmetric_difference(uniqaln_slova2)
print(f"Слова, которые присутствуют только в одном из текстов:", ednstvennoe)