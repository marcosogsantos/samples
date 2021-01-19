import os
def files_of_directory(directory,type_of_file):
    path = directory
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.'+type_of_file in file:
                files.append(os.path.join(r, file))
    return files