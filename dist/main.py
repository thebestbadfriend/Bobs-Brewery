from global_tools import config as cfg
from global_tools import default_updater as du
from core.ui import WindowWrapper


def main():
    print("Note: closing this window will close Bob's Brewery.")

    release_info = du.get_latest_github_release(cfg.REPO_NAME)
    print(f"The latest release is {release_info['version']}")
    print(f"It can be downloaded from {release_info['download_url']}")

    root = WindowWrapper.load_window_from_file(rf"{cfg.SOURCE_ROOT}\core\ui\ui_elements\windows\main_window.json")
    root.window.mainloop()


main()
