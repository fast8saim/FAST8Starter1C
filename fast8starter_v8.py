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
        self.name = name.strip()


def parse_ibases(text):
    bases_list = []

    item = None
    for line in text:
        if line.startswith("["):
            if len(bases_list) == 4:
                break
            if item is not None:
                bases_list.append(item)
            item = V8Base(line.replace('[', '').replace(']', ''))
        if item is not None:
            if line.startswith("ID"):
                item.ID = line.replace('ID=', '').strip()
            elif line.startswith("OrderInList"):
                item.OrderInList = line.replace('OrderInList=', '').strip()
            elif line.startswith("Folder"):
                item.Folder = line.replace('Folder=', '').strip()
            elif line.startswith("OrderInTree"):
                item.OrderInTree = line.replace('OrderInTree=', '').strip()
            elif line.startswith("External"):
                item.External = line.replace('External=', '').strip()
            elif line.startswith("Connect"):
                item.Connect = line.replace('Connect=', '').strip()
            elif line.startswith("Ref"):
                item.Ref = line.replace('Ref=', '').strip()
            elif line.startswith("ClientConnectionSpeed"):
                item.ClientConnectionSpeed = line.replace('ClientConnectionSpeed=', '').strip()
            elif line.startswith("App"):
                item.App = line.replace('App=', '').strip()
            elif line.startswith("WA"):
                item.WA = line.replace('WA=', '').strip()
            elif line.startswith("Version"):
                item.Version = line.replace('Version=', '').strip()
            elif line.startswith("DefaultVersion"):
                item.DefaultVersion = line.replace('DefaultVersion=', '').strip()
            elif line.startswith("AppArch"):
                item.AppArch = line.replace('AppArch=', '').strip()
            elif line.startswith("AdditionalParameters"):
                item.AdditionalParameters = line.replace('AdditionalParameters=', '').strip()

    if item is not None:
        bases_list.append(item)

    return bases_list
