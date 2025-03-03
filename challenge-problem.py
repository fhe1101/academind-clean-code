# (c) Maximilian Schwarzmüller / Academind GmbH

# <-- legal comments are all right

# --> these marks and dividers are bad, should be removed.
# *********
# Imports
# *********
from os import path, makedirs
from pathlib import Path

# *********
# Main
# *********

# --> this is not a valid documentation. If needed, use python standard documentation style

# A class which allows us to create DiskStorage instances

class DiskStorage:
    def __init__(self, directory_name):
        self.storage_directory = directory_name

    def get_directory_path(self):
        return Path(self.storage_directory)

    # --> warnings can make sense. this is not what the code will fail.
    # This must be called before a file is inserted
    def create_directory(self):
        if (not path.exists(self.get_directory_path())):
            makedirs(self.storage_directory)

    # --> still not the best place
    # Warning: Directory must exist in advance
    def insert_file(self, file_name, content):
        # --> opportunity to reduce horizontal space for this line
        file = open(self.get_directory_path() / file_name, 'w')
        file.write(content)
        file.close()

        # -> this is ok in a short term.
        # Todo: Add proper error handling


# these two lines do not need line spacing
log_storage = DiskStorage('logs')

log_storage.insert_file('test.txt', 'Test')
