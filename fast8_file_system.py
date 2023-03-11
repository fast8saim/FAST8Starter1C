# fast8_file_system.py

import os

def get_ibases_content():
    file_bases = os.getcwd() + "\\Application Data\\1C\\1CEStart\\ibases.v8i"
    if os.path.exists(file_bases):
        text = open(file_bases, encoding = "utf").readlines()
    else:
        text = ""

    return text