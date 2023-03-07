from loaders.html_loader import HtmlLoader
from pipelines.text_processor import TextProcessor
from pipelines.indexer import DavinciConfigLLM, IndexLoader, interact_with_user
from capabilties.interfaces import ConvInterface
import os
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_URL = os.environ["WEAVIATE_URL"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

path = f"data/index/{DavinciConfigLLM.name}.json"

index = IndexLoader(config=DavinciConfigLLM, load_from_location=path)

# interact_with_user(index.llm_index)
conv_ai = ConvInterface(llm_index=index.llm_index)
conv_ai()
