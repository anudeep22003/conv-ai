from loaders.html_loader import HtmlLoader
from pipelines.text_processor import TextProcessor
from pipelines.indexer import DavinciConfigLLM, Indexer, interact_with_user
import os
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_URL = os.environ["WEAVIATE_URL"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

path = "data"

document_index = HtmlLoader(path_to_url_list="misc/url_list.txt").extract_text(
    path=f"{path}/doc_index.json"
)
cleaned_document_index = TextProcessor(
    directory="data", file_name="doc_index.json"
).clean()

index = Indexer(
    document_index=cleaned_document_index,
    config=DavinciConfigLLM,
    save_location_path="data/index",
)

interact_with_user(index.llm_index)
