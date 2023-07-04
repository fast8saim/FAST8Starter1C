# fast8_engine_v8.py

import os


class V8Base:
    ID = ''
    OrderInList = 0
    Folder = ''
    OrderInTree = 0
    External = 0
    Connect = ''
    Ref = ''
    ClientConnectionSpeed = 'Normal'
    App = 'Auto'
    WA = 1
    Version = '8.3'
    DefaultVersion = '8.3'
    AppArch = 'x86_64'
    AdditionalParameters = ''

    def __init__(self, name):
        self.name = name


def find_platform():
    path = 'C:'
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("1cv8.exe"):
                path_file = os.path.join(root, file)
                print(path_file)


def parse_ibases(text):
    bases_list = []

    item = None
    for line in text:
        if line.startswith("["):
            if item is not None:
                bases_list.append(item)
            item = V8Base(line.replace('[', '').replace(']', ''))
        if item is not None:
            if line.startswith("ID"):
                item.ID = line.replace('ID=', '')
            elif line.startswith("OrderInList"):
                item.OrderInList = line.replace('OrderInList=', '')
            elif line.startswith("Folder"):
                item.Folder = line.replace('Folder=', '')
            elif line.startswith("OrderInTree"):
                item.OrderInTree = line.replace('OrderInTree=', '')
            elif line.startswith("External"):
                item.External = line.replace('External=', '')
            elif line.startswith("Connect"):
                item.Connect = line.replace('Connect=', '')
            elif line.startswith("Ref"):
                item.Ref = line.replace('Ref=', '')
            elif line.startswith("ClientConnectionSpeed"):
                item.ClientConnectionSpeed = line.replace('ClientConnectionSpeed=', '')
            elif line.startswith("App"):
                item.App = line.replace('App=', '')
            elif line.startswith("WA"):
                item.WA = line.replace('WA=', '')
            elif line.startswith("Version"):
                item.Version = line.replace('Version=', '')
            elif line.startswith("DefaultVersion"):
                item.DefaultVersion = line.replace('DefaultVersion=', '')
            elif line.startswith("AppArch"):
                item.AppArch = line.replace('AppArch=', '')
            elif line.startswith("AdditionalParameters"):
                item.AdditionalParameters = line.replace('AdditionalParameters=', '')

    if item is not None:
        bases_list.append(item)

    return bases_list
