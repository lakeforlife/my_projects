text = input("Введите ваш текст: ")
for i in text:
    if i.isdigit():
        text = text.replace(i, "")
for i in [".", ",", "!", "?", ":", ";", ")", "(", "\"", "\'", "-", "«", "»", "– ", "\n", "\r", "  ", "— "]:
    if i in text:
        text = text.replace(i, "")
s_text = text.split(" ")
dlina = 0
samoe_dlinnoe = ""
count = 0
samoe_chastoe = ""
for i in s_text:
    if len(i) > dlina:
        dlina = len(i)
        samoe_dlinnoe = i
    if s_text.count(i) > count:
        count = s_text.count(i)
        samoe_chastoe = i
print(f"\nСамое частое слово в тексте: \"{samoe_chastoe}\", встречается {count} раз(-а)")
print(f"Самое длинное слово в тексте: \"{samoe_dlinnoe}\", его длина {dlina} букв(-ы)")
