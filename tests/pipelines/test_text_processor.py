import pytest, json
from src.loaders.directory_loader import Loader
from src.pipelines.text_processor import TextProcessor

fixture_path = "tests/fixtures/text_cleaning_fixture.json"


@pytest.fixture
def text_processor():
    tp = TextProcessor()
    yield tp
    del tp


def test_remove_linebreak(text_processor):
    with open(file=fixture_path, mode="r") as f:
        d = json.load(f)
    assert text_processor.remove_linebreak(d["file1"]) == "Word single, double"


def test_remove_multiple_nextline(text_processor):
    with open(file=fixture_path, mode="r") as f:
        d = json.load(f)
    assert (
        text_processor.remove_multiple_nextlines(d["file2"])
        == "Single\nDouble\nMultiple\n"
    )
