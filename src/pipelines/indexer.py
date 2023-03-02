from llama_index import Document, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from typing import List, Dict, Any
from langchain import OpenAI
from pprint import pprint


class ConfigLLM:
    # define LLM
    name = "ada-003"
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001"))

    # define prompt helper
    # set maximum input size
    max_input_size = 2048
    # set number of output tokens
    num_output = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)


class DavinciConfigLLM:
    # define LLM
    name = "davinci-003"
    llm_predictor = LLMPredictor(
        llm=OpenAI(temperature=0, model_name="text-davinci-003")
    )

    # define prompt helper
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_output = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap)


class Indexer:
    "Index the data using llama_index"

    def __init__(
        self,
        document_index: dict,
        save_location_path: str,
        config: ConfigLLM = ConfigLLM,
    ) -> None:
        self.doc_index = document_index
        self.config = config
        self.llm_index = self.construct_index()
        self.save_index(save_location_path=save_location_path)

    def load_index(self, index_path: str) -> Any:
        return GPTSimpleVectorIndex.load_from_dist(index_path)

    def save_index(self, save_location_path: str) -> None:
        save_file_path = f"{save_location_path}/{self.config.name}.json"
        self.llm_index.save_to_disk(save_file_path)

    def construct_index(
        self,
    ) -> List[Document]:
        assert bool(self.doc_index), "document index is empty"
        # documents constructed using llama_index document constructor
        documents = [Document(doc) for id, doc in self.doc_index.items()]
        return GPTSimpleVectorIndex(
            documents,
            llm_predictor=self.config.llm_predictor,
            prompt_helper=self.config.prompt_helper,
        )


class IndexLoader:
    "Index the data using llama_index"

    def __init__(
        self,
        load_from_location: str = None,
        config: ConfigLLM = ConfigLLM,
    ) -> None:
        self.config = config
        self.llm_index = self.load_index(load_from_location)

    def load_index(self, index_path: str) -> Any:
        return GPTSimpleVectorIndex.load_from_disk(index_path)


def interact_with_user(
    llm_index: dict,
):
    end_request = ["q", "x", "exit"]
    modes = {1: "default", 2: "compact", 3: "tree_summarize"}
    while True:
        user_query = input("Ask your query --> ")
        if user_query.lower() in end_request:
            break
        while True:
            user_response_mode = input(
                "\nWhich mode do you choose: \n (1) default\t(2) compact\t(3) tree_summarize\n q: quit\n--> "
            )
            if user_response_mode in end_request:
                break
            try:
                user_response_mode = int(user_response_mode)
            except Exception as e:
                print("Invalid choice, try again")
                continue
            response = llm_index.query(
                user_query, response_mode=modes[user_response_mode]
            )
            print(f"mode: {modes[user_response_mode]} \nresponse: {response}\n\n")
            pprint(response.get_formatted_sources())
