# GITLAB BACKUP SCRIPT

## Usage:
0. Create a virtual environment => `python3 -m virtualenv .venv`
0. Activate your virtual environment => `source .venv/bin/active # Windows: ./.venv/Scripts/activate.bat`
0. Install dependencies => `pip install -r requirements.txt`
0. Fill up `config.py` file.
0. Run `python export_repos_urls.py [SSH|HTTP]`, Use SSH if you have SSH Keys, otherwise use HTTP
0. Run `download_exports.py`
