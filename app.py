import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text",  server_port=10000, server_name="0.0.0.0")
demo.launch()
