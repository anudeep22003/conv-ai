import gradio as gr
from typing import Any, Tuple, List


class ConvInterface:
    "class to build a conversational interface using gradio"

    def __init__(self, llm_index) -> None:
        self.index = llm_index
        pass

    def update_context(self, state_user, state_ai) -> str:
        "Builds the context that gets chained to the next llm query"
        context = []
        for user_q, ai_respone in zip(state_user, state_ai):
            inline_context = f"""
            User Query:
            {str(user_q)}

            AI Response:
            {str(ai_respone)}

            """
            context.append(inline_context)
        meta_context = "Given the previous User Query and the AI Response, answer the below User Query."
        context.append(meta_context)
        return "\n".join(context)

    def converse(self, state_user, state_ai, text) -> List:
        "where the user input is being taken mixed with historic context and output being generated for chatbot to display"
        state_user += [text]
        context = self.update_context(state_user, state_ai)
        response = self.index.query(f"{context}\n{text}")
        state_ai += [f"{response}"]
        state_merged = list(zip(state_user, state_ai))
        return state_user, state_ai, state_merged

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        "overload this to build the query"
        with gr.Blocks() as demo:
            chatbot = gr.Chatbot()
            state_user = gr.State([])
            state_ai = gr.State([])

            with gr.Row():
                with gr.Column():
                    txt = gr.Textbox(
                        show_label=False, placeholder="Enter text and press enter"
                    )

                    txt.submit(
                        fn=self.converse,
                        inputs=[state_user, state_ai, txt],
                        outputs=[state_user, state_ai, chatbot],
                        show_progress=True,
                    )
        demo.launch()


if __name__ == "__main__":
    c = ConvInterface(None)
    c()
