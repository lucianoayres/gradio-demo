import gradio as gr


def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


demo = gr.Interface(fn=greet, inputs=["text", "slider"], outputs="text")

# Launch the application with public URL
# The app will run locally directly from your machine
# A public URL will be assigned
demo.launch(share=True)
