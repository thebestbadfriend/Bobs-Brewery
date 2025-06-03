import os
import json
import sys
import subprocess
import config as cfg

import concealed_vars as cv



def fix_server_access():
    os.system('net use * /delete /y > NUL')
    os.system(rf'net use Z: \\PAT-PC\MiTek_Network /user:bt3 "{cv.COMMON_PASS}"')
    os.system(rf'net use Y: "\\bt-server\Alpine Data" /user:bt-user "{cv.COMMON_PASS}"')
    os.system('net use')


def open_favorite_programs():
    with open(rf'{cfg.source_root}\core\dal\favorite_programs.json', 'r') as favorite_programs_file:
        data = json.load(favorite_programs_file)

        for program in data:
            subprocess.Popen(program['path'], shell=True)


def add_contact():
    pass


def on_btn_exit_click():
    sys.exit()
