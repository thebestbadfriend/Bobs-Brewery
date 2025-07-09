import os

from global_tools import config as global_cfg
from global_tools import default_updater as du
from core import config as core_cfg
from core.ui import WindowWrapper


def main():
    print("Note: closing this window will close Bob's Brewery.")

    release_info = du.check_latest_github_release(global_cfg.REPO_NAME)
    print(f"The latest release is {release_info['version']}")
    print(f"It can be downloaded from {release_info['download_url']}")

    if release_info['version'] != core_cfg.CORE_VERSION:
        stage = os.path.join(os.environ["TEMP"], "bobs-brewery-stage")
        dest = rf"Bobs-Brewery-v{release_info['version']}.zip"
        du.download_latest_github_release(release_info['download_url'], stage, dest)
        du.extract_update(stage, dest)

        # run updater.py with appropriate args
        # exit this process immediately to avoid file locks
    else:
        print('Already using latest version!')

    root = WindowWrapper.load_window_from_file(rf"{global_cfg.SOURCE_ROOT}\core\ui\ui_elements\windows\main_window.json")
    root.window.mainloop()


main()
