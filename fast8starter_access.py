from pykeepass import PyKeePass

DATABASE_NAME = 'fast8_1cpass.kdbx'


def read_access(base, master_password):
    kp = PyKeePass(filename=DATABASE_NAME, password=master_password)
    for e in kp.entries:
        pass
