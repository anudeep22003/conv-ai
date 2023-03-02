import re, json


class TextProcessor:
    """
    Clean the text
    """

    def __init__(self, directory: str, file_name: str) -> None:
        self.dir = directory
        self.f_name = file_name
        pass

    def clean(self) -> None:
        fpath = self.dir + "/" + self.f_name
        doc_index = self.read_file(fpath)
        clean_doc_index = self.iterate_and_clean(doc_index)
        self.write_to_file(clean_doc_index, f"{self.dir}/cleaned_{self.f_name}")

    def iterate_and_clean(self, doc_index: dict) -> dict:
        for idx, doc in doc_index.items():
            cleaned_doc = self.remove_multiple_nextlines(doc)
            cleaned_doc = self.remove_linebreak(doc)
            doc_index[idx] = cleaned_doc
        return doc_index

    def read_file(
        self,
        file_path: str,
    ) -> dict:
        with open(file=file_path, mode="r", encoding="utf-8") as f:
            return json.load(f)

    def write_to_file(
        self,
        write_obj: dict,
        file_path: str,
    ) -> None:
        with open(file=f"{file_path}", mode="a", encoding="utf-8") as f:
            json.dump(write_obj, f)

    def remove_linebreak(self, doc: str) -> dict:
        "remove \u00a0 character"
        return re.sub(r"\s+", " ", doc)

    def remove_multiple_nextlines(self, doc: str) -> dict:
        "remove \n\n occuring multiple times"
        return re.sub(r"\n+", "\n", doc)


if __name__ == "__main__":
    tp = TextProcessor(directory="misc", file_name="blog_index.json")
    tp.clean()
