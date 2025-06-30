import argparse


parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument('version')
args = parser.parse_args()

url = args.url
version = args.version

print(f"url: {url}")
print(f"version: {version}")