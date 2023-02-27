from loaders.loader import Loader
from pipelines.text_processor import TextProcessor
from pipelines.indexer import ConfigLLM, Indexer
import os
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_URL = os.environ["WEAVIATE_URL"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

path = "data/"

document_index = Loader().extract_text(path=path)
document_index = TextProcessor().remove_newline(doc_index=document_index)

interactive_index = Indexer(document_index=document_index)

interactive_index.interact_with_user()
