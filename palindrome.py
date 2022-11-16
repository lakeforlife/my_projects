print("НАЙДЕМ ПАЛИНДРОМ?")
print("Чтобы завершить, введите \"конец\"\n")
while True:
    text = input("Введите ваше слово: ").lower()
    if text.isalpha():
        if text == text[::-1] and text != "":
            print("Поздравляем, это палиндром!")
        else:
            if text == "конец":
                break
            print("Упс, это не палиндром")
    else:
        print("Ошибка, введите одно слово, без цифр и пробелов")
print("Спасибо за участие в программе")
