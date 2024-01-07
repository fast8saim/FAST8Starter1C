import os


def get_ibases_content():
    home_dir = os.environ['USERPROFILE']
    file_bases = home_dir + "\\Application Data\\1C\\1CEStart\\ibases.v8i"
    print(file_bases)
    if os.path.exists(file_bases):
        text = open(file_bases, encoding="utf").readlines()
    else:
        text = ""

    return text
