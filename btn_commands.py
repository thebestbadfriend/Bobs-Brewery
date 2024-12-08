import os
import json


def fix_server_access():
    os.system("net use * /delete /y")
    os.system("net use Z: \\\\PAT-PC\\MiTek_Network")
    os.system("net use")


def open_favorite_programs():
    with open("favorite_programs.json", "r") as favorite_programs_file:
        data = json.load(favorite_programs_file)

        for program in data:
            os.system(program["path"])


def add_contact():
    pass