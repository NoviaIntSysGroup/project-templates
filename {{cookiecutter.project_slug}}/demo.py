import gradio as gr
from {{ cookiecutter.package_name }}.hello import hello

def greet(name: str, intensity: str) -> str:
    return hello(name) + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
