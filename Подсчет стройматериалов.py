print("\nПРОГРАММА ПОДСЧЕТА КОЛИЧЕСТВА МАТЕРИАЛА ДЛЯ РЕМОНТА\n")


def my_input():
    while True:
        i = input()
        if i.isdigit() and int(i) > 0:
            return int(i)
        else:
            print("Ошибка, надо ввести целое число > 0: ", end="")


print("Введите высоту стены (см): ", end="")
h_sten = my_input()
print("Введите длину стены (см): ", end="")
l_sten = my_input()
print("Введите высоту материала (см): ", end="")
h_mat = my_input()
print("Введите длину материала (см): ", end="")
l_mat = my_input()

s_sten_sm = h_sten * l_sten
s_sten_m = round((h_sten * l_sten * 0.0001), 2)
s_mat_sm = h_mat * l_mat
s_mat_m = h_mat * l_mat * 0.0001
kolvo_mat = round((s_sten_sm / s_mat_sm), 2)

print("У вас будет разделительный шов? 1 - да, 2 - нет: ", end="")
shov = my_input()
if shov == 1:
    print("Введите толщину разделительного шва (мм): ", end="")
    l_shva = my_input()
    s_shva_sm = (h_mat + l_mat) * (l_shva / 10)
    s_shvov_m = s_shva_sm * kolvo_mat * 0.0001
    kolvo_mat_shva = (s_sten_m - s_shvov_m) / s_mat_m
    
print("\nОБЩАЯ ПЛОЩАДЬ СТЕНЫ: ", s_sten_m, "м2")
print("ПЛОЩАДЬ ОДНОГО МАТЕРИАЛА: ", round(s_mat_m, 5), "м2")
print("ОБЩЕЕ КОЛИЧЕСТВО МАТЕРИАЛА: ", round(kolvo_mat, 2), "шт.")
if shov == 1:
    print("ОБЩАЯ ПЛОЩАДЬ ШВОВ: ", round(s_shvov_m, 2), "м2")
    print("ОБЩЕЕ КОЛИЧЕСТВО МАТЕРИАЛА С УЧЕТОМ ШВОВ: ", round(kolvo_mat_shva, 2), "шт.")

try:
    file = open("Подсчеты.txt", 'a', encoding='utf-8')
    file.write(f"\nОБЩАЯ ПЛОЩАДЬ СТЕНЫ: {s_sten_m} м2\n"
               f"ОБЩЕЕ КОЛИЧЕСТВО МАТЕРИАЛА: {kolvo_mat} шт.\n")
except Exception as e:
    print("\nОшибка записи файла:", e)
finally:
    file.close()