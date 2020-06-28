import os


def count_dirs_and_files(directory='.') -> tuple:
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    # dirs = len([item for item in os.listdir(directory) if os.path.isdir(os.path.join(directory, item))])
    # files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])
    dirs = 0
    files = 0
    for _, dirnames, filenames in os.walk(directory):
        dirs += len(dirnames)
        files += len(filenames)
    return (dirs, files)
