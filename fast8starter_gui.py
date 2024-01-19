import flet as ft
from fast8starter_data import Bases, Platforms


class AccessDialog(ft.UserControl):
    page = None
    base = None
    dialog = None

    def fill(self):
        pass

    def __init__(self, page: ft.Page, base):
        super().__init__()
        self.page = page
        self.base = base
        self.controls = self.build()

    def build(self):
        self.dialog = ft.AlertDialog()
        self.dialog.open = True
        data_table = ft.DataTable()
        self.dialog.content = data_table
        return data_table


class BasesList(ft.UserControl):
    page = None
    bases_column = None
    platform = None

    def run_thick_client(self, e):
        print('ThickClient')

    def run_legacy_client(self, e):
        print('LegacyClient')

    def run_designer(self, e):
        print('Designer')

    def run_update_from_storage(self, e):
        print('UpdateFromStorage')

    def run_save_configuration(self, e):
        print('SaveConfiguration')

    def run_upload_configuration(self, e):
        print('UploadConfiguration')

    def run_save_dump(self, e):
        print('SaveDump')

    def run_upload_dump(self, e):
        print('UploadDump')

    def run_reconnect_to_storage(self, e):
        print('ReconnectToStorage')

    def run_save_extensions(self, e):
        print('SaveExtensions')

    def run_upload_extensions(self, e):
        print('UploadExtensions')

    def run_clear_cache(self, e):
        print('ClearCache')

    def open_access(self, e):
        pass

    def run_thin_client(self, e):
        base = e.control.data
        base.run_client(self.platform)

    def copy_base_path(self, e):
        self.page.set_clipboard(value=e.control.data.connect)

    def fill(self):
        self.bases_column.controls.clear()
        bases = Bases()
        bases.fill()

        for base in bases.list:
            self.bases_column.controls.append(
                ft.Card(shape=ft.RoundedRectangleBorder(radius=4),
                        content=ft.Column([
                            ft.Row([
                                ft.Text(f' {bases.list.index(base) + 1}. {base.name}')]),
                            ft.Row([
                                ft.Text(f'  {base.connect}')]),
                            ft.Row([
                                ft.IconButton(icon=ft.icons.DOMAIN, icon_color=ft.colors.YELLOW, tooltip='Предприятие',
                                              on_click=self.run_thin_client, data=base),
                                ft.IconButton(icon=ft.icons.HANDYMAN, icon_color=ft.colors.YELLOW,
                                              tooltip='Конфигуратор',
                                              on_click=self.run_designer),
                                ft.IconButton(icon=ft.icons.MODE, icon_color=ft.colors.YELLOW, tooltip='Редактировать'),
                                ft.IconButton(icon=ft.icons.KEY, icon_color=ft.colors.YELLOW, tooltip='Доступ', data=base, on_click=self.open_access),
                                ft.IconButton(icon=ft.icons.TEXT_SNIPPET, icon_color=ft.colors.YELLOW,
                                              tooltip='Сценарий'),
                                ft.Container(expand=True),
                                ft.IconButton(icon=ft.icons.COPY, icon_color=ft.colors.YELLOW,
                                              tooltip='Копировать в буфер', data=base, on_click=self.copy_base_path),
                                ft.PopupMenuButton(tooltip='Дополнительно',
                                                   items=[
                                                       ft.PopupMenuItem(
                                                           content=ft.Text('Толстый клиент', color=ft.colors.YELLOW),
                                                           on_click=self.run_thick_client),
                                                       ft.PopupMenuItem(text='Обычное приложение',
                                                                        on_click=self.run_legacy_client),
                                                       ft.PopupMenuItem(text='Обновить из хранилища',
                                                                        on_click=self.run_update_from_storage),
                                                       ft.PopupMenuItem(text='Сохранить конфигурацию',
                                                                        on_click=self.run_save_configuration),
                                                       ft.PopupMenuItem(text='Загрузить конфигурацию',
                                                                        on_click=self.run_upload_configuration),
                                                       ft.PopupMenuItem(text='Выгрузить в dt', on_click=self.run_save_dump),
                                                       ft.PopupMenuItem(text='Загрузить из dt',
                                                                        on_click=self.run_upload_dump),
                                                       ft.PopupMenuItem(text='Переподключить к хранилищу',
                                                                        on_click=self.run_reconnect_to_storage),
                                                       ft.PopupMenuItem(text='Выгрузить расширения',
                                                                        on_click=self.run_save_extensions),
                                                       ft.PopupMenuItem(text='Загрузить расширения',
                                                                        on_click=self.run_upload_extensions),
                                                       ft.PopupMenuItem(text='Очистить кэш метаданных',
                                                                        on_click=self.run_clear_cache)
                                                   ])
                            ])])))
        self.page.update()

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.controls = self.build()

    def build(self):
        self.bases_column = ft.ListView(expand=True, spacing=1, padding=1, auto_scroll=False, width=500)
        self.page.add(self.bases_column)

        return self.bases_column


def main_frame(page: ft.Page):
    page.title = 'FAST8 STARTER 1C'
    page.theme_mode = 'dark'
    page.window_width = 500
    page.window_opacity = 0.8

    def run_make_clean_base(event):
        print('MakeCleanBase')

    def run_find_local_file_bases(event):
        print('FindLocalFileBases')

    def run_clear_all_cache(event):
        print('ClearAllCache')

    bases_list = BasesList(page)
    bases_list.fill()

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE_GREY_900,
        width=500,
        content=ft.Row([
            ft.IconButton(icon=ft.icons.ADD, tooltip='Добавить новую базу'),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.icons.ADD, icon_color=ft.colors.YELLOW, tooltip='Создать чистую базу',
                          on_click=run_make_clean_base),
            ft.IconButton(icon=ft.icons.FIND_IN_PAGE, icon_color=ft.colors.YELLOW, tooltip='Найти файловые базы',
                          on_click=run_find_local_file_bases),
            ft.IconButton(icon=ft.icons.DELETE, icon_color=ft.colors.YELLOW, tooltip='Очистить весь локальный кэш',
                          on_click=run_clear_all_cache),
            ft.IconButton(icon=ft.icons.SETTINGS, icon_color=ft.colors.YELLOW, tooltip='Настройки'),
        ])
    )

    page.update()
    platforms = Platforms()
    platforms.fill()
    bases_list.platform = platforms.default_platform


def create_gui():
    ft.app(target=main_frame)
