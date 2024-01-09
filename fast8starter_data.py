import fast8starter_system


class Platform:
    version = ''
    bin32 = ''
    bin64 = ''

    def __init__(self, version: str):
        self.version = version


class Platforms:
    default_platform = None
    list = []

    def __init__(self):
        self.list = []

    def fill(self):
        entries = fast8starter_system.find_platform()
        for entry in entries:
            platform = Platform(entry)
            self.list.append(platform)


class Base:
    name = ''
    base_id = ''
    order_in_list = 0
    folder = ''
    order_in_tree = 0
    external = 0
    connect = ''
    ref = ''
    client_connection_speed = 'Normal'
    app = 'Auto'
    wa = 1
    version = '8.3'
    default_version = '8.3'
    app_arch = 'x86_64'
    additional_parameters = ''

    def __init__(self, name):
        self.name = name.strip()

    def fill(self, entry: dict):
        self.base_id = entry.get('base_id')
        self.order_in_list = entry.get('order_in_list')
        self.folder = entry.get('folder')
        self.order_in_tree = entry.get('order_in_tree')
        self.external = entry.get('external')
        self.connect = entry.get('connect')
        self.ref = entry.get('ref')
        self.client_connection_speed = entry.get('client_connection_speed')
        self.app = entry.get('app')
        self.wa = entry.get('wa')
        self.version = entry.get('version')
        self.default_version = entry.get('default_version')
        self.app_arch = entry.get('app_arch')
        self.additional_parameters = entry.get('additional_parameters')


class Bases:
    list = []

    def __init__(self):
        self.list = []

    def sort(self):
        self.list.sort(key=lambda e: e.name)

    def add_entry(self, entry):
        if 'connect' in entry:
            base = Base(entry.get('name'))
            base.fill(entry)
            self.list.append(base)

    def fill(self):
        keys = {
            'ID=': 'base_id',
            'OrderInList=': 'order_in_list',
            'Folder=': 'folder',
            'OrderInTree=': 'order_in_tree',
            'External=': 'external',
            'Connect=': 'connect',
            'Ref=': 'ref',
            'ClientConnectionSpeed=': 'client_connection_speed',
            'App=': 'app',
            'WA=': 'wa',
            'Version=': 'version',
            'DefaultVersion=': 'default_version',
            'AppArch=': 'app_arch',
            'AdditionalParameters=': 'additional_parameters'
        }

        text = fast8starter_system.get_ibases_content()
        entry = None
        for line in text:
            if line.startswith("["):
                if entry is not None:
                    self.add_entry(entry)
                entry = {}
                entry.setdefault('name', line.replace('[', '').replace(']', ''))
            if entry is not None:
                for key in keys:
                    if line.startswith(key):
                        entry.setdefault(keys.get(key), line.replace(key, '').strip())

        if entry is not None:
            self.add_entry(entry)

        self.sort()
