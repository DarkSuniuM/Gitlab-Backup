"""Export Your Gitlab Repos URLs."""

import sys

from requests import Session

from config import (ACCESS_TOKEN, BASE_URL, PASSWORD, URLS_EXPORT_PATH,
                    USER_ID, USERNAME)

LINK_TYPES = {'ssh': 'ssh_url_to_repo', 'http': 'http_url_to_repo'}
LINK_TYPE = LINK_TYPES.get(sys.argv[-1].lower(), None)

if not LINK_TYPE:
    print('Specify link type for generating URLs:'
          '\n    python export_repos_urls.py ssh'
          '\n    python export_repos_urls.py http')
    exit(1)

session = Session()
session.headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}


def generate_url(endpoint: str) -> str:
    """Generate Endpoint URL."""
    return f'{BASE_URL}{endpoint}'


def get_user_projects(user_id: str) -> list:
    """Get user projects."""
    projects = []
    URL = generate_url('projects')
    id_after = None

    def get_projects_list(id_after=None):
        return session.get(URL,
                           params={
                               'pagination': 'keyset',
                               'per_page': 100,
                               'order_by': 'id',
                               'id_after': id_after,
                               'sort': 'asc',
                               'membership': 'true'
                           })

    while resp := get_projects_list(id_after).json():
        if not isinstance(resp, list):
            break
        if len(resp) == 0:
            break
        projects += resp
        id_after = projects[-1]['id']
    return projects


def generate_clone_url(repo: dict):
    """Generate Clone URL for Repository."""
    clone_url = repo[LINK_TYPE]
    if USERNAME and PASSWORD:
        clone_url = clone_url.replace('https://gitlab',
                                      f'https://{USERNAME}:{PASSWORD}@gitlab')
    return clone_url + '\n'


projects = get_user_projects(user_id=USER_ID)
with open(URLS_EXPORT_PATH, 'w') as file:
    file.writelines(map(generate_clone_url, projects))
