import glob
import os

# All the paths are relative to the root latex file directory

PATH = 0
FILE_NAME = 1

path_file_pairs = []
files_to_exclude = ["notes.pdf", "notes.tex"]
paths_to_files_in_src = glob.glob("./*.*")

for path in paths_to_files_in_src:
    path_segments = path.split("/")
    file_name = path_segments[len(path_segments) - 1]
    if file_name not in files_to_exclude:
        path_file_pairs.append((path, file_name))

for path_file_pair in path_file_pairs:
    os.rename(path_file_pair[PATH], "../tmp/" + path_file_pair[FILE_NAME])