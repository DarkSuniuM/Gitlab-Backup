"""Configuration file."""

import os
from urllib.parse import quote

# Get from https://gitlab.com/profile/personal_access_tokens, Give all permissions
ACCESS_TOKEN = ''

# Get from https://gitlab.com/profile
USER_ID = ''

# ONLY REQUIRED IF YOU DO HTTP CLONE, Your Gitlab Username
USERNAME = quote('')

# ONLY REQUIRED IF YOU DO HTTP CLONE, Your Gitlab Password
PASSWORD = quote('')

# Don't change it if you wanna use Gitlab.com
BASE_URL = 'https://gitlab.com/api/v4/'

# Path to save your repositories URLs
URLS_EXPORT_PATH = os.path.normpath(os.path.abspath('./repos.txt'))

# Path to clone your repositories
BACKUP_DIR = os.path.normpath(os.path.abspath('./backup'))
