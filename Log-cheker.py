import tkinter as tk
import tkinter.filedialog as fd
from tkinter.filedialog import askopenfilename

win = tk.Tk()
win.title("Анализ LOG-файлов")
win.geometry("800x600")
my_list_ip = {}
my_list_source = {}


def log_analiser():
    """
    Очищает все поля программы. Получает лог-файл, указанный пользователем,
    находит в нем все уникальные ip, источники запросов, их количество
    и выводит в упорядоченном виде.
    """
    counter = 0
    global my_list_ip
    filename = fd.askopenfilename()

    text_ip.delete("1.0", "end")
    text_source.delete("1.0", "end")
    text_info.delete("1.0", "end")

    with open(filename, "r") as f:

        for Line in f:
            ip = Line.split(" ")[0]
            source = Line.split('"')[-2]
            counter += 1

            if ip not in my_list_ip:
                my_list_ip[ip] = 1
            else:
                my_list_ip[ip] += 1

            if source not in my_list_source:
                my_list_source[source] = 1
            else:
                my_list_source[source] += 1

    my_list_sort_ip = sorted(my_list_ip.items(), key=lambda x: x[1])
    my_list_sort_source = sorted(my_list_source.items(), key=lambda x: x[1])
    text_info.insert(1.0, f"Общее количество запросов: {str(counter)}")

    for i in my_list_sort_ip:
        (ip_in_list, count_ip) = i
        text_ip.insert(1.0, f'{ip_in_list} - {count_ip}\n')

    for i in my_list_sort_source:
        (source_in_list, source_count) = i
        text_source.insert(1.0, f'{source_in_list} - {source_count}\n\n')


block_1 = tk.Label(win, text='Выберите файл для начала анализа.\n Данная программа покажет список ip, а также список источников запросов.', pady=20)
but_1 = tk.Button(win, text="Открыть log-файл", command=log_analiser)
text_info = tk.Text(win, wrap='word', height=1, width=100, padx=20)
text_ip = tk.Text(win, wrap='word', height=12, width=100, padx=20)
text_source = tk.Text(win, wrap='word', height=12, width=100, padx=20)

block_1.pack()
but_1.pack()
text_info.pack()
text_ip.pack()
text_source.pack()

win.mainloop()
