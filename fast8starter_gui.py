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
    page.window_width = 500
    page.window_opacity = 0.8

    def create_label(label):
        return ft.Text(label)

    def create_button(label, procedure):
        return ft.ElevatedButton(text=label, on_click=procedure)

    bases_list = fast8starter_v8.parse_ibases(fast8starter_system.get_ibases_content())

    bases_column = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=False, width=500)
    page.add(bases_column)

    for item in bases_list:
        bases_column.controls.append(
            ft.Column([
                ft.Row([
                    ft.Text(item.name)]),
                ft.Row([
                    ft.IconButton(icon=ft.icons.DOMAIN, icon_color=ft.colors.YELLOW, tooltip='Предприятие', on_click=run_thin_client),
                    ft.IconButton(icon=ft.icons.HANDYMAN, icon_color=ft.colors.YELLOW, tooltip='Конфигуратор', on_click=run_designer),
                    ft.IconButton(icon=ft.icons.MODE, icon_color=ft.colors.YELLOW, tooltip='Редактировать'),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.COPY, icon_color=ft.colors.YELLOW, tooltip='Копировать в буфер'),
                    ft.PopupMenuButton(tooltip='Дополнительно',
                                       items=[
                                           ft.PopupMenuItem(content=ft.Text('Толстый клиент', color=ft.colors.YELLOW), on_click=run_thick_client),
                                           ft.PopupMenuItem(text='Обычное приложение', on_click=run_legacy_client),
                                           ft.PopupMenuItem(text='Обновить из хранилища',
                                                            on_click=run_update_from_storage),
                                           ft.PopupMenuItem(text='Сохранить конфигурацию',
                                                            on_click=run_save_configuration),
                                           ft.PopupMenuItem(text='Загрузить конфигурацию',
                                                            on_click=run_upload_configuration),
                                           ft.PopupMenuItem(text='Выгрузить в dt', on_click=run_save_dump),
                                           ft.PopupMenuItem(text='Загрузить из dt', on_click=run_upload_dump),
                                           ft.PopupMenuItem(text='Переподключить к хранилищу',
                                                            on_click=run_reconnect_to_storage),
                                           ft.PopupMenuItem(text='Выгрузить расширения', on_click=run_save_extensions),
                                           ft.PopupMenuItem(text='Загрузить расширения',
                                                            on_click=run_upload_extensions),
                                           ft.PopupMenuItem(text='Очистить кэш метаданных', on_click=run_clear_cache)
                                       ])
                ])]))
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE_GREY_900,
        width=500,
        content=ft.Row([
            ft.IconButton(icon=ft.icons.ADD, tooltip='Добавить новую базу'),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.icons.ADD, icon_color=ft.colors.YELLOW, tooltip='Создать чистую базу', on_click=run_make_clean_base),
            ft.IconButton(icon=ft.icons.FIND_IN_PAGE, icon_color=ft.colors.YELLOW, tooltip='Найти файловые базы',
                          on_click=run_find_local_file_bases),
            ft.IconButton(icon=ft.icons.DELETE, icon_color=ft.colors.YELLOW, tooltip='Очистить весь локальный кэш', on_click=run_clear_all_cache),
            ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.YELLOW, tooltip='Настройки'),
        ])
    )

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
    ft.app(target=main_frame)
