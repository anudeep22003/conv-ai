import os
from pprint import pprint


class Loader:
    """
    Responsibility: To extract data from a data source and pass it into the pipeline for processing
    Do the following:
    read_file --> convert from markdown to text --> return dictionary mapping of title and text
    """

    def __init__(self) -> None:
        pass

    def extract_text(self, path: str) -> dict:
        filelist = self.get_files_from_directory(path)
        return self.read_files(filelist)

    def get_files_from_directory(self, path) -> list:
        # check if directory is found
        file_list = []
        for file_path in os.listdir(path=path):
            if os.path.isfile(f"{path}{file_path}"):
                file_list.append(f"{path}{file_path}")

        return file_list

    def read_files(self, file_list) -> dict:
        document_index = {}
        for f_path in file_list:
            with open(f_path, "r") as f:
                document_index[f_path] = "".join(f.readlines())
        return document_index


if __name__ == "__main__":
    path = "data/"
    l = Loader()
    pprint(l.extract_text(path))
