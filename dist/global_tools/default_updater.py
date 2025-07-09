import global_tools.config as cfg
import os
import requests
import zipfile


def check_latest_github_release(repo):
    print("Checking Github Releases for latest version")

    url = f"https://api.github.com/repos/{cfg.REPO_OWNER}/{repo}/releases/latest"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "version": data["tag_name"],
            "download_url": data["zipball_url"]
        }
    except Exception as e:
        print(f"Error getting latest release: {e}")
        return None


def download_latest_github_release(url, dest_dir, dest_file):
    print("Downloading latest version")
    dest = rf"{dest_dir}\{dest_file}"
    response = requests.get(url, stream=True)
    response.raise_for_status()

    os.makedirs(dest_dir, exist_ok=True)
    with open(dest, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk: f.write(chunk)


def extract_update(stage_dir, stage_file):
    stage_path = rf"{stage_dir}\{stage_file}"
    with zipfile.ZipFile(stage_path, 'r') as zip_ref:
        zip_ref.extractall(rf"{stage_dir}\bobs-brewery-extracted-update")
