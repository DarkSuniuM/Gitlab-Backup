"""Clone Git Repos from Exported URLs."""

import os
import pathlib

import subprocess as sp

from config import BACKUP_DIR, URLS_EXPORT_PATH

if not os.path.exists(BACKUP_DIR):
    os.mkdir(BACKUP_DIR)


def generate_project_backup_path(project_name: str) -> str:
    """Generate CrossPlatform Compatible Path."""
    project_name = project_name.replace('@', '_at_').replace(':', '__')
    return os.path.normpath(
        os.path.abspath(os.path.join(BACKUP_DIR, project_name)))


with open(URLS_EXPORT_PATH, 'r') as file:
    repos = file.read().strip('\n').split('\n')

for index, line in enumerate(repos):
    project_name = line.split('gitlab.com/')[-1]
    project_backup_path = generate_project_backup_path(project_name)
    print(f'{index}/{len(repos)} => {project_name}')
    sp.check_output(['git', 'clone', line, project_backup_path])
    print()
    print()
