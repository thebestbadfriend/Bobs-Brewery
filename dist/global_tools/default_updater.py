import global_tools.config as cfg
import requests

def get_latest_github_release(repo):
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
