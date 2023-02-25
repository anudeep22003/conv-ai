class TextProcessor:
    """
    Clean the text
    """

    def __init__(self) -> None:
        pass

    def remove_newline(self, doc_index: dict) -> dict:
        for index, docstring in doc_index.items():
            modified_docstring = docstring.replace("\n\n", ". ")
            modified_docstring = modified_docstring.replace("\n", " ")
            modified_docstring = modified_docstring.replace("\\", "")
            doc_index[index] = modified_docstring
        return doc_index
