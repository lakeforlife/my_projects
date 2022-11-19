key, key_student = "", ""
my_groups = {}
students = []
while True:
    key = input("Введите название группы (ENTER, чтобы завершить): ")
    if key == "":
        break
    else:
        students.clear()
        my_groups[key] = None
        while True:
            key_student = input(f"Фамилия и имя ({key}): ")
            if key_student == "":
                break
            else:
                students.append(key_student)

    my_groups[key] = students.copy()

print(my_groups)





