import os
import sys


def delete_file(filename, directory_position):
    for root, directories, files in os.walk(directory_position):
        for file in files:
            if file == filename:
                os.remove(os.path.join(root, file))
                print(f"Deleted: {os.path.join(root, file)}")


if len(sys.argv) == 3:
    delete_file(sys.argv[1], sys.argv[2])
else:
    Exception(f"Not enough arguments")
