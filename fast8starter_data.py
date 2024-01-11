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

    def sort(self):
        self.list.sort(key=lambda e: e.version)

    def __init__(self):
        self.list = []

    def fill(self):
        entries = fast8starter_system.find_platform()
        for entry in entries:
            platform = Platform(entry)
            self.list.append(platform)

        self.sort()
        self.default_platform = self.list[len(self.list) - 1]


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
    is_file = False
    connection_string = ''

    def run_client(self, platform: Platform):
        fast8starter_system.run_process(f'{platform.version} ENTERPRISE {self.connection_string}')

    def __init__(self, name):
        self.name = name.strip()

    def fill(self, entry: dict):
        if 'base_id' in entry:
            self.base_id = entry.get('base_id')
        if 'order_in_list' in entry:
            self.order_in_list = entry.get('order_in_list')
        if 'folder' in entry:
            self.folder = entry.get('folder')
        if 'order_in_tree' in entry:
            self.order_in_tree = entry.get('order_in_tree')
        if 'external' in entry:
            self.external = entry.get('external')
        if 'connect' in entry:
            self.connect = entry.get('connect')
        if 'ref' in entry:
            self.ref = entry.get('ref')
        if 'client_connection_speed' in entry:
            self.client_connection_speed = entry.get('client_connection_speed')
        if 'app' in entry:
            self.app = entry.get('app')
        if 'wa' in entry:
            self.wa = entry.get('wa')
        if 'version' in entry:
            self.version = entry.get('version')
        if 'default_version' in entry:
            self.default_version = entry.get('default_version')
        if 'app_arch' in entry:
            self.app_arch = entry.get('app_arch')
        if 'additional_parameters' in entry:
            self.additional_parameters = entry.get('additional_parameters')

        if self.connect:
            self.is_file = True if self.connect.startswith('File=') else False
            if self.is_file:
                self.connection_string = self.connect[6:-2].strip()
            else:
                ref_pos = self.connect.find('Ref=')
                self.connection_string = f'/S {self.connect[6:ref_pos - 2]}\\{self.connect[ref_pos + 5:-2]}'


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
