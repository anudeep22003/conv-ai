import gradio as gr
from typing import Any, Tuple, List


class ConvInterface:
    "class to build a conversational interface using gradio"

    def __init__(self, llm_index) -> None:
        self.index = llm_index
        pass

    def update_conversation(self, state, text) -> List:
        response = self.index.query(text)
        state = state + [(text, str(response))]
        return state, state

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        "overload this to build the query"
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            state = gr.State([])

            with gr.Row():
                with gr.Column():
                    txt = gr.Textbox(
                        show_label=False, placeholder="Enter text and press enter"
                    )

            txt.submit(
                fn=self.update_conversation,
                inputs=[state, txt],
                outputs=[state, chatbot],
            )
        demo.launch()


if __name__ == "__main__":
    c = ConvInterface(None)
    c()
