# fast8_interface

import wx
import subprocess


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
    dlg = wx.DirDialog(None, 'Выбор директории', 'C:\\python_projects', wx.DD_DEFAULT_STYLE)
    res = dlg.ShowModal()

    if res == wx.ID_OK:
        print('MakeCleanBase', dlg.GetPath())


def run_find_local_file_bases(event):
    print('FindLocalFileBases')


def run_clear_all_cache(event):
    dlg = wx.MessageDialog(None, 'Очистить всё?', 'Очистка кэша', wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION)

    res = dlg.ShowModal()
    if res == wx.ID_YES:
        print('ClearAllCache')


class MainFrame(wx.Frame):

    def create_label(self, label):
        new_label = wx.StaticText(self.panel, label=label)
        self.vbox.Add(new_label, flag=wx.ALL, border=1)

    def create_button(self, label, procedure):
        new_button = wx.Button(self.panel, label=label, size=(200, 25))
        self.vbox.Add(new_button, flag=wx.ALL, border=1)
        new_button.Bind(wx.EVT_BUTTON, procedure)

    def __init__(self, parent, title):
        super().__init__(parent, title=title, style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,
                         size=(500, 530))

        self.panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        self.create_label("Предприятие")
        self.create_button("Тонкий клиент", run_thin_client)
        self.create_button("Толстый клиент", run_thick_client)
        self.create_button("Обычное приложение", run_legacy_client)

        self.create_label("Конфигуратор")
        self.create_button("Конфигуратор", run_designer)
        self.create_button("Обновить из хранилища", run_update_from_storage)
        self.create_button("Сохранить конфигурацию", run_save_configuration)
        self.create_button("Загрузить конфигурацию", run_upload_configuration)
        self.create_button("Выгрузить в dt", run_save_dump)
        self.create_button("Загрузить из dt", run_upload_dump)
        self.create_button("Переподключить к хранилищу", run_reconnect_to_storage)
        self.create_button("Выгрузить расширения", run_save_extensions)
        self.create_button("Загрузить расширения", run_upload_extensions)

        self.create_label("Прочее")
        self.create_button("Очистить кэш метаданных", run_clear_cache)
        self.create_button("Создать чистую базу", run_make_clean_base)
        self.create_button("Найти файловые базы", run_find_local_file_bases)
        self.create_button("Очистить весь локальный кэш", run_clear_all_cache)

        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        #self.list_bases = wx.ListBox(self.panel, size=(100, 485))
        self.list_bases = wx.ListCtrl(self.panel, -1, style=wx.LC_ICON | wx.LC_AUTOARRANGE, size=(100, 485))

        self.hbox.Add(self.list_bases, flag=wx.ALL, border=1, proportion=1)
        self.hbox.Add(self.vbox, flag=wx.ALL, border=1)
        self.panel.SetSizer(self.hbox)


def create_main_window(bases_list):
    app = wx.App()

    frame = MainFrame(None, 'FAST8 STARTER 1C')
    frame.Centre()
    frame.Show()

    for item in bases_list:
        frame.list_bases.InsertItem(bases_list.index(item), item['name'])

    # из буфера обмена
    # cb = root.clipboard_get()

    app.MainLoop()
