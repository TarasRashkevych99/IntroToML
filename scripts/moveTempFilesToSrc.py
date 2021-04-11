import glob
import os

# All the paths are relative to the root latex file directory

PATH = 0
FILE_NAME = 1

if os.path.isdir("../tmp/"):
    path_file_pairs = []
    paths_to_files_in_tmp = glob.glob("../tmp/*")

    for path in paths_to_files_in_tmp:
        path_segments = path.split("/")
        file_name = path_segments[len(path_segments) - 1]
        path_file_pairs.append((path, file_name))

    for path_file_pair in path_file_pairs:
        os.rename(path_file_pair[PATH], "./" + path_file_pair[FILE_NAME])
else:
    os.mkdir("../tmp/")
