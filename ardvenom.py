#!/bin/env python
import argparse
from os import system


def perror(error):
    print(f'[ERROR] {error}')
    exit(1)

def get_setup(os, lib_name):
    if os == 'osx':
        perror("not implemented yet :(")
    if os == 'windows':
        setup = "[LIB].press(KEY_LEFT_GUI);" \
                "[LIB].press('r');" \
                "[LIB].releaseAll();"
    if os == 'linux':
        setup = "[LIB].press(KEY_LEFT_CTRL);" \
                "[LIB].press(KEY_LEFT_ALT);" \
                "[LIB].press('t');" \
                "[LIB].releaseAll();"
    return setup.replace('[LIB]', lib_name)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--os", required=True, help="Target OS")
    ap.add_argument("-l", "--layout", required=True, help="Target keyboard layout")
    ap.add_argument("-c", "--cmd", required=True, help="Command to execute")
    args = vars(ap.parse_args())

    cmd = args['cmd']
    os = args['os'].lower()
    layout = args['layout'].lower()

    if os not in ['windows', 'osx', 'linux']:
        perror("OS must be Window, OSX or Linux")
    if layout not in ['azerty', 'qwerty']:
        perror("Layout must be azerty or qwerty")

    lib = 'Keyboard.h' if layout == 'qwerty' else 'KeyboardAzertyFr.h'
    lib_name = lib.split('.h')[0]
    lib_ver = lib_name if layout == 'qwerty' else f'{lib_name}@1.0.1'
    setup = get_setup(os, lib_name)

    with open('./arduino/Ardvenom.ino', 'r') as template:
        tmp_ino = template.read()
        tmp_ino = tmp_ino.replace('[LIB_H]', lib)
        tmp_ino = tmp_ino.replace('[LIB]', lib_name)
        tmp_ino = tmp_ino.replace('[HOOK]', setup)
        tmp_ino = tmp_ino.replace('[CMD]', cmd)

    with open('./Makefile.default', 'r') as makefile:
        tmp_makefile = makefile.read()
        tmp_makefile = tmp_makefile.replace('[LIB]', lib_ver)

    with open('./Makefile', 'w') as makefile:
        makefile.write(tmp_makefile)

    with open('./tmp.ino', 'w') as payload:
        payload.write(tmp_ino)

    system('make upload')

