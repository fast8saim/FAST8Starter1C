# fast8_form_create.py

import tkinter
from tkinter import ttk
import subprocess


# from PIL import Image, ImageTk


def run_thin_client():
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')


def run_thick_client():
    print('ThickClient')


def run_legacy_client():
    print('LegacyClient')


def run_designer():
    print('Designer')


def run_update_from_storage():
    print('UpdateFromStorage')


def run_save_configuration():
    print('SaveConfiguration')


def run_upload_configuration():
    print('UploadConfiguration')


def run_save_dump():
    print('SaveDump')


def run_upload_dump():
    print('UploadDump')


def run_reconnect_to_storage():
    print('ReconnectToStorage')


def run_save_extensions():
    print('SaveExtensions')


def run_upload_extensions():
    print('UploadExtensions')


def run_clear_cache():
    print('ClearCache')


def run_make_clean_base():
    print('MakeCleanBase')


def run_find_local_file_bases():
    print('FindLocalFileBases')


def run_clear_all_cache():
    print('ClearAllCache')


def create_base_list(form, root, bases_list):
    listbox = ttk.Treeview(form, show="headings", columns=("#1"), height=19)
    listbox.column("#1", width=400)
    listbox.grid(column=0, row=0, rowspan=19)
    listbox.heading("#1", text="База")
    ysb = ttk.Scrollbar(root, command=listbox.yview)
    listbox.configure(yscroll=ysb.set)

    for item in bases_list:
        listbox.insert(parent=item['parent'], index=bases_list.index(item), values=item['name'])


def create_button(form, button_text, button_column, button_row, button_width, button_command):
    button = ttk.Button(form)
    button['width'] = button_width
    button['text'] = button_text
    button['command'] = button_command
    button.grid(column=button_column, row=button_row)


def create_label(form, label_text, label_column, label_row):
    label = ttk.Label(form)
    label['text'] = label_text
    label.grid(column=label_column, row=label_row)


def create_main_form(bases_list):
    root = tkinter.Tk()
    root.title("FAST8 Стартер 1С")
    form = ttk.Frame(root, padding=5)
    form.grid()

    create_base_list(form, root, bases_list)

    # logo = Image.open('logo.png')
    # logo = ImageTk.PhotoImage(logo)
    # logo_label = tkinter.label(image=logo)
    # logo_label.image = logo
    # logo_label.grid(column=1, row=1)

    create_label(form, "Предприятие", 1, 1)
    create_button(form, "Тонкий клиент", 1, 2, 30, run_thin_client)
    create_button(form, "Толстый клиент", 1, 3, 30, run_thick_client)
    create_button(form, "Обычное приложение", 1, 4, 30, run_legacy_client)

    create_label(form, "Конфигуратор", 1, 5)
    create_button(form, "Конфигуратор", 1, 6, 30, run_designer)
    create_button(form, "Обновить из хранилища", 1, 7, 30, run_update_from_storage)
    create_button(form, "Сохранить конфигурацию", 1, 8, 30, run_save_configuration)
    create_button(form, "Загрузить конфигурацию", 1, 9, 30, run_upload_configuration)
    create_button(form, "Выгрузить в dt", 1, 10, 30, run_save_dump)
    create_button(form, "Загрузить из dt", 1, 11, 30, run_upload_dump)
    create_button(form, "Переподключить к хранилищу", 1, 12, 30, run_reconnect_to_storage)
    create_button(form, "Выгрузить расширения", 1, 13, 30, run_save_extensions)
    create_button(form, "Загрузить расширения", 1, 14, 30, run_upload_extensions)

    create_label(form, "Прочее", 1, 15)
    create_button(form, "Очистить кэш метаданных", 1, 16, 30, run_clear_cache)
    create_button(form, "Создать чистую базу", 1, 17, 30, run_make_clean_base)
    create_button(form, "Найти файловые базы на компьютере", 1, 18, 30, run_find_local_file_bases)
    create_button(form, "Очистить весь локальный кэш", 1, 19, 30, run_clear_all_cache)

    # из буфера обмена
    # cb = root.clipboard_get()

    root.mainloop()
