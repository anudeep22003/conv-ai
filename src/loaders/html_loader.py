from typing import List, Dict, Any
from llama_index import download_loader
import urllib.request
from bs4 import BeautifulSoup
import json

simple_web_page_reader = download_loader("SimpleWebPageReader")


class HtmlLoader:
    "load data from my personal blog"

    def __init__(self, path_to_url_list: str, debug: bool = True) -> None:
        self.reader = simple_web_page_reader()
        self.debug = debug
        self.path_to_url_list = path_to_url_list
        self.doc_index = {}
        pass

    def get_url_list(self, path_to_url_list) -> List[str]:
        "get list of urls from the text list of urls"
        with open(file=path_to_url_list, mode="r") as f:
            url_list = f.readlines()
        return url_list

    def request_url(self, url: str) -> str:
        "uses urllib library to download the relevant html"
        html_file = urllib.request.urlopen(url)
        html_file_text = html_file.read().decode("utf-8")
        if self.debug:
            with open("misc/html_output.html", "a", encoding="utf-8") as f:
                f.write(html_file_text)
        return html_file_text

    def create_soup(self, url: str) -> Any:
        "takes in a html file and outputs a list of ahref links"
        html_text = self.request_url(url)
        return url, BeautifulSoup(html_text, "html.parser")

    def read_urls(self, url: str, soup) -> Dict[str, str]:
        "read the text in the soup and add to document index"
        post_body_tag = soup.select_one(".post-body")
        if post_body_tag is not None:
            text_list = [str(string) for string in post_body_tag.stripped_strings]
            self.doc_index[url] = "\n".join(text_list)

    def extract_text(self, path: str) -> Dict[str, str]:
        url_list = self.get_url_list(self.path_to_url_list)
        for url in url_list:
            doc_url, soup = self.create_soup(url)
            self.read_urls(doc_url, soup)
        self.write_to_file(write_path=path)
        return self.doc_index

    def write_to_file(self, write_path: str) -> None:
        "write to file, this will serve as input for text cleaning"
        with open(file=write_path, mode="w", encoding="utf-8") as f:
            json.dump(self.doc_index, f)


if __name__ == "__main__":
    h = HtmlLoader(path_to_url_list="misc/url_list.txt", debug=True)
    h.extract_text()
