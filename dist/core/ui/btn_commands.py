import os
import json

import sys
import subprocess
from global_tools import config as cfg
import core.config as core_cfg

import concealed_vars as cv


def check_for_updates():
    print("Checking for updates...")
    url = f"https://api.github.com/repos/{cfg.REPO_OWNER}/{cfg.REPO_NAME}/releases/latest"
    latest_version = '0.1.1' # change this to pull latest version from github's api

    if core_cfg.CORE_VERSION == latest_version:
        print('You are up to date!')


def fix_server_access():
    os.system('net use * /delete /y > NUL')
    os.system(rf'net use Z: \\PAT-PC\MiTek_Network /user:bt3 "{cv.COMMON_PASS}"')
    os.system(rf'net use Y: "\\bt-server\Alpine Data" /user:bt-user "{cv.COMMON_PASS}"')
    os.system('net use')


def open_favorite_programs():
    with open(rf'{cfg.SOURCE_ROOT}\core\dal\favorite_programs.json', 'r') as favorite_programs_file:
        data = json.load(favorite_programs_file)

        for program in data:
            subprocess.Popen(program['path'], shell=True)


def add_contact():
    pass


def on_btn_exit_click():
    sys.exit()
