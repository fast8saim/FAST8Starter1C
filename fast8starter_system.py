import os
import glob
import subprocess


def run_process(url):
    subprocess.Popen(url)


def get_ibases_content():
    home_dir = os.environ['USERPROFILE']
    file_bases = home_dir + "\\Application Data\\1C\\1CEStart\\ibases.v8i"

    if os.path.exists(file_bases):
        text = open(file_bases, encoding="utf").readlines()
    else:
        text = ""

    return text


def find_platform():
    paths = []
    for res in glob.glob('c:\\Program Files\\**\\1cv8.exe', recursive=True):
        paths.append(res)
        print(res)

    return paths

