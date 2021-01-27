from datetime import datetime
from pathlib import Path, PosixPath
from zipfile import ZipFile

TMP = Path('/tmp')
LOG_DIR = TMP / 'logs'
ZIP_FILE = 'logs.zip'


def zip_last_n_files(directory: PosixPath = LOG_DIR,
                     zip_file: str = ZIP_FILE,
                     n: int = 3):
    # Get most recent n timestamps
    most_rec_updates = sorted([f.stat().st_mtime for f in directory.iterdir()],
                              reverse=True)[:n]
    # Get files according to most recent timestamps
    files = [file for file in directory.iterdir()
             if file.stat().st_mtime in most_rec_updates]
    # Rename files and add to new list
    new_files = []
    for file in files:
        dt_str = datetime.fromtimestamp(
            file.stat().st_mtime
            ).strftime('%Y-%m-%d')
        pre, suf = file.name.split('.')
        new_name = f'{pre}_{dt_str}.{suf}'

        Path(file).replace(Path(new_name))
        new_files.append(Path(new_name))
    # Write new_files list to ZipFile
    with ZipFile(zip_file, 'w') as myzip:
        for file in new_files:
            myzip.write(file)
