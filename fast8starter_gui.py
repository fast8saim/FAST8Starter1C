import flet as ft
import subprocess
import fast8starter_system
import fast8starter_v8

def run_thin_client(event):
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')


def run_thick_client(event):
    print('ThickClient')


def run_legacy_client(event):
    print('LegacyClient')


def run_designer(event):
    print('Designer')


def run_update_from_storage(event):
    print('UpdateFromStorage')


def run_save_configuration(event):
    print('SaveConfiguration')


def run_upload_configuration(event):
    print('UploadConfiguration')


def run_save_dump(event):
    print('SaveDump')


def run_upload_dump(event):
    print('UploadDump')


def run_reconnect_to_storage(event):
    print('ReconnectToStorage')


def run_save_extensions(event):
    print('SaveExtensions')


def run_upload_extensions(event):
    print('UploadExtensions')


def run_clear_cache(event):
    print('ClearCache')


def run_make_clean_base(event):
    """dlg = wx.DirDialog(None, 'Выбор директории', 'C:\\python_projects', wx.DD_DEFAULT_STYLE)
    res = dlg.ShowModal()

    if res == wx.ID_OK:
        print('MakeCleanBase', dlg.GetPath())"""


def run_find_local_file_bases(event):
    print('FindLocalFileBases')


def run_clear_all_cache(event):
    """dlg = wx.MessageDialog(None, 'Очистить всё?', 'Очистка кэша', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION)

    res = dlg.ShowModal()
    if res == wx.ID_YES:
        print('ClearAllCache')"""


def main_frame(page: ft.Page):

    page.title = 'FAST8 STARTER 1C'
    page.theme_mode = 'dark'

    def create_label(label):
        return ft.Text(label)

    def create_button(label, procedure):
        return ft.ElevatedButton(text=label, on_click=procedure)

    bases_list = fast8starter_v8.parse_ibases(fast8starter_system.get_ibases_content())

    bases_column = ft.Column()
    buttons_column = ft.Column()

    page.add(ft.Row(
        [
            bases_column, buttons_column
        ])
    )

    for item in bases_list:
        bases_column.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.HOME_WORK),
                                title=ft.Text(item.name),
                                subtitle=ft.Text(item.AppArch),
                            ),
                            ft.Row(
                                [ft.TextButton("Run"), ft.TextButton("Configure")],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=500, padding=5,
                )
            )
        )

    buttons_column.controls.append(create_label("Предприятие"))
    buttons_column.controls.append(create_button("Тонкий клиент", run_thin_client))
    buttons_column.controls.append(create_button("Толстый клиент", run_thick_client))
    buttons_column.controls.append(create_button("Обычное приложение", run_legacy_client))
    buttons_column.controls.append(create_label("Конфигуратор"))
    buttons_column.controls.append(create_button("Конфигуратор", run_designer))
    buttons_column.controls.append(create_button("Обновить из хранилища", run_update_from_storage))
    buttons_column.controls.append(create_button("Сохранить конфигурацию", run_save_configuration))
    buttons_column.controls.append(create_button("Загрузить конфигурацию", run_upload_configuration))
    buttons_column.controls.append(create_button("Выгрузить в dt", run_save_dump))
    buttons_column.controls.append(create_button("Загрузить из dt", run_upload_dump))
    buttons_column.controls.append(create_button("Переподключить к хранилищу", run_reconnect_to_storage))
    buttons_column.controls.append(create_button("Выгрузить расширения", run_save_extensions))
    buttons_column.controls.append(create_button("Загрузить расширения", run_upload_extensions))
    buttons_column.controls.append(create_label("Прочее"))
    buttons_column.controls.append(create_button("Очистить кэш метаданных", run_clear_cache))
    buttons_column.controls.append(create_button("Создать чистую базу", run_make_clean_base))
    buttons_column.controls.append(create_button("Найти файловые базы", run_find_local_file_bases))
    buttons_column.controls.append(create_button("Очистить весь локальный кэш", run_clear_all_cache))

    page.update()
    """
    # из буфера обмена
    # cb = root.clipboard_get()
    
    def __init__(self, parent, title):
        super().__init__(parent, title=title, style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,
                         size=(600, 530))
        self.list_bases = wx.ListCtrl(self.panel, -1, style=wx.LC_REPORT, size=(100, 485))
        self.list_bases.InsertColumn(0, 'Базы')
        self.list_bases.SetColumnWidth(0, 360)

        self.hbox.Add(self.list_bases, flag=wx.ALL, border=1, proportion=1)
        self.hbox.Add(self.vbox, flag=wx.ALL, border=1)
        self.panel.SetSizer(self.hbox)"""


def create_gui():
    fast8starter_system.find_platform()
    ft.app(target=main_frame)
