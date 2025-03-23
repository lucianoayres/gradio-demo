---
title: gradio-demo
app_file: app.py
sdk: gradio
sdk_version: 5.22.0
---

# Gradio: Demo for Machine Learning Web Apps in Python

Gradio is an open-source Python library that makes it easy to create customizable, interactive web interfaces for machine learning models. It enables you to build demos rapidly without requiring extensive web development expertise. With Gradio, you can share your models with collaborators or the public, test them live, and even deploy them on cloud platforms for free. Its intuitive interface and simple API allow you to focus on your model rather than the underlying infrastructure.

## Benefits of Using Gradio

- **User-Friendly Interfaces:** Quickly generate interactive demos that allow users to experiment with machine learning models.
- **Ease of Integration:** Integrate with popular frameworks like TensorFlow, PyTorch, and scikit-learn.
- **Rapid Prototyping:** Build and iterate on your model’s interface in minutes.
- **Shareability:** Easily share your demos via public URLs that can be generated with a single command.
- **Deployment Options:** Deploy on local servers, cloud services, or platforms like Hugging Face Spaces for free hosting and GPU access.

## Installation

Follow these steps to set up the project environment:

1. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

3. **Install Gradio:**

   ```bash
   pip install --upgrade gradio
   ```

## Usage

1. **Run the application:**

   ```bash
   python app.py
   ```

2. **Open the URL in your browser:**

   ```bash
   open http://localhost:7860
   ```

3. **Interact with the app:**  
   Use the interface and optionally click the **Flag** button to save data to a local dataset located at `.gradio/flagged/dataset1.csv`.

## Running in Hot Reload Mode

For live modifications, run the app with Gradio’s built-in hot-reload feature:

```bash
gradio app.py
```

## Deployment

### Temporary Public URL

Deploy your app with a public URL by passing the optional parameter `share=True` to the `launch` method in your code:

```python
demo.launch(share=True)
```

_Note: The share link expires in 72 hours._

### Permanent Hosting on Hugging Face Spaces

For free, permanent hosting with GPU support, deploy your app on [Hugging Face Spaces](https://huggingface.co/spaces):

```bash
gradio deploy
```

> **IMPORTANT:** To proceed, you'll need an access token with **Write** permission on Hugging Face. If you haven't generated one yet, please [create one here](https://huggingface.co/settings/tokens).

Project URL on Hugging Face:
[https://huggingface.co/spaces/layers2024/gradio-demo](https://huggingface.co/spaces/layers2024/gradio-demo)

## References & Resources

- [Gradio GitHub Repository](https://github.com/gradio-app/gradio)
- [Gradio Documentation](https://gradio.app/)
