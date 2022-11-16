print("ПОИСК ПАЛИНДРОМОВ В ТЕКСТЕ\n")

text = input("Введите ваш текст: ")
for i in text:
    if i.isdigit():
        text = text.replace(i, "")
for i in [".", ",", "!", "?", ":", ";", ")", "(", "\"", "\'", "-", "«", "»", "– ", "\n", "\r", "  ", "— "]:
    if i in text:
        text = text.replace(i, "")

text = text.lower()
text = text.split(" ")

my_count = 0
for i in text:
    if i == i[::-1] and i !="" and len(i) != 1:
        print("Палиндром: ", i)
        my_count += 1
        if my_count == 0:
            print("В вашем тексте нет слов-палиндромов")
print("Количество найденных палиндромов: ", my_count)
