import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textSummarization"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb"
]

for files in list_of_files:
    file_path = Path(files)
    filedirectory, filename = os.path.split(file_path)

    if filedirectory != "":
        os.makedirs(filedirectory, exist_ok=True)
        logging.info(f"File: {filename} is located in the directory: {filedirectory}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w'):
            pass
            logging.info(f"Creating empty file: {file_path}")
    
    else:
        logging.info(f"File: {filename} already exists in the directory: {filedirectory}")
        