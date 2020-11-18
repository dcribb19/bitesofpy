import glob
import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    return [file for file in glob.glob(f'{dirname}/*')
            if os.stat(file).st_size >= size_in_kb * ONE_KB]
