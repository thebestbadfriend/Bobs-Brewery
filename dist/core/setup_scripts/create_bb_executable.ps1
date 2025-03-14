# Nuitka does not work with python3.13 yet. Need to make sure python3.12 is installed in appdata\local\programs\python
# If it is, then I can just add the interpreter here. The option for that in settings even handles creation of a venv
# and there can be multiple venvs, such as at brewers I have a 3.13 ".venv" and a 3.12 ".venv3.12"

nuitka --standalone --onefile --enable-plugin=tk-inter --include-package=psycopg main.py

# the above compiles but 'no pq wrapper'
# the below is a recommendation from chatgpt
# seeing if it works

nuitka --standalone --onefile --enable-plugin=tk-inter --include-package=psycopg --include-package=psycopg.pq main.py
