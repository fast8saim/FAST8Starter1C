import os


def get_ibases_content():
    home_dir = os.environ['USERPROFILE']
    file_bases = home_dir + "\\Application Data\\1C\\1CEStart\\ibases.v8i"

    if os.path.exists(file_bases):
        text = open(file_bases, encoding="utf").readlines()
    else:
        text = ""

    return text


def find_platform():
    path = 'C:\\Program Files'
    for root, dirs, files in os.walk(path):
        for file in files:
            #if file.endswith("1cv8.exe"):
            if file == '1cv8.exe':
                path_file = os.path.join(root, file)
                print(path_file)
