# fast8_engine_v8.py

import os
    
def find_platform():
    path = 'C:'
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith("1cv8.exe"):
                path_file = os.path.join(root,file)
                print(path_file)

def parse_ibases(text):
    bases_list = []
    
    for line in text:
        if line.startswith("["):
            item = {'name': line.replace('[', '').replace(']', ''), 'parent': ''}
            bases_list.append(item)

    return bases_list