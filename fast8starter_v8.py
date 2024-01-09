class V8Base:
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

    def __setitem__(self, key, value):
        if key == 'base_id':
            self.base_id = value
        elif key == 'order_in_list':
            self.order_in_list = value
        elif key == 'folder':
            self.folder = value
        elif key == 'order_in_tree':
            self.order_in_tree = value
        elif key == 'external':
            self.external = value
        elif key == 'connect':
            self.connect = value
        elif key == 'ref':
            self.ref = value
        elif key == 'client_connection_speed':
            self.client_connection_speed = value
        elif key == 'app':
            self.app = value
        elif key == 'wa':
            self.wa = value
        elif key == 'version':
            self.version = value
        elif key == 'default_version':
            self.default_version = value
        elif key == 'app_arch':
            self.app_arch = value
        elif key == 'additional_parameters':
            self.additional_parameters = value


def parse_ibases(text):
    bases_list = []

    keys = {
        'ID': 'base_id',
        'OrderInList': 'order_in_list',
        'Folder': 'folder',
        'OrderInTree': 'order_in_tree',
        'External': 'external',
        'Connect': 'connect',
        'Ref': 'ref',
        'ClientConnectionSpeed': 'client_connection_speed',
        'App': 'app',
        'WA': 'wa',
        'Version': 'version',
        'DefaultVersion': 'default_version',
        'AppArch': 'app_arch',
        'AdditionalParameters': 'additional_parameters'
    }

    item = None
    for line in text:
        if line.startswith("["):
            if item is not None:
                bases_list.append(item)
            item = V8Base(line.replace('[', '').replace(']', ''))
        if item is not None:
            for key in keys:
                if line.startswith(key):
                    item[keys.get(key)] = line.replace(key, '').strip()

    if item is not None:
        bases_list.append(item)

    return bases_list
