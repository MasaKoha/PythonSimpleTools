import os


def delete_file(filename, directory_position):
    for root, directories, files in os.walk(directory_position):
        for file in files:
            if file == filename:
                os.remove(os.path.join(root, file))
                print(f"Deleted: {os.path.join(root, file)}")


delete_file(".DS_Store", "./")
