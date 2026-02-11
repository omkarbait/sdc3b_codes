import os

def get_nonempty_subdirs(parent_dir):
    """
    Returns a list of subdirectory names in parent_dir that contain at least one file.
    """
    subdirs_with_files = []
    for subdir in os.listdir(parent_dir):
        subdir_path = os.path.join(parent_dir, subdir)
        if os.path.isdir(subdir_path):
            # Check if there is at least one file in the subdir
            if any(os.path.isfile(os.path.join(subdir_path, f)) for f in os.listdir(subdir_path)):
                subdirs_with_files.append(subdir)
    return subdirs_with_files

# Example usage:
# parent_directory = "/path/to/submissions"
# print(get_nonempty_subdirs(parent_directory))
