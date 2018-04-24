import os
from zipfile import ZipFile
from pathlib import Path


def properly_unzip_files():
    """
    Given that `Branch_user_logs.zip` exists in the data directory, this will unzip Branch users into that directory

    :returns:
    Hierarchy of [user_id]/[device_id] in the data directory
    """

    path_to_zip_file = "./data/Branch_user_logs.zip"
    directory_to_extract_to = "./data/"
    does_dir_exist = Path("./data/user_logs/")

    if os.path.exists(does_dir_exist):
        print("Files already exist")
    else:
        try:
            print("Unzipping files into the data directory")
            zip_ref = ZipFile(path_to_zip_file, "r")
            zip_ref.extractall(directory_to_extract_to)
            zip_ref.close()

        except IOError as e:
            print(
                "Unable to open file either because it doesn't exist or you don't have read permission"
            )


if __name__ == "__main__":
    properly_unzip_files()
