# Gradio: Demo

## Machine Learning Web Apps in Python

Gradio is an open-source Python library that makes it simple to create interactive, customizable web interfaces for your machine learning models. It allows you to build demos rapidly—without requiring extensive web development expertise—and share them easily with collaborators or the public. With Gradio, you can test your models live and even deploy them on cloud platforms for free, letting you focus on your model rather than the underlying infrastructure.

## Benefits of Using Gradio

- **User-Friendly Interfaces:** Generate interactive demos quickly so users can experiment with your models.
- **Ease of Integration:** Works seamlessly with popular frameworks such as TensorFlow, PyTorch, and scikit-learn.
- **Rapid Prototyping:** Build and iterate on your model’s interface in minutes.
- **Shareability:** Instantly share demos via public URLs with just one command.
- **Flexible Deployment:** Deploy on local servers, cloud services, or platforms like Hugging Face Spaces for free hosting and even GPU support.

## Installation

Set up your project environment with the following steps:

1. **Create a Virtual Environment:**

   ```bash
   python -m venv .venv
   ```

2. **Activate the Virtual Environment:**

   ```bash
   source .venv/bin/activate
   ```

3. **Install Gradio:**

   ```bash
   pip install --upgrade gradio
   ```

## Usage

1. **Run the Application:**

   ```bash
   python app.py
   ```

2. **Open the URL in Your Browser:**

   ```bash
   open http://localhost:7860
   ```

3. **Interact with the App:**  
   Use the interface and, if desired, click the **Flag** button to save data to a local dataset located at `.gradio/flagged/dataset1.csv`.

## Running in Hot Reload Mode

For live modifications, run your app with Gradio’s hot-reload feature:

```bash
gradio app.py
```

## Deployment

### Temporary Public URL

Deploy your app with a public URL by setting the `share` parameter to `True` in your launch method:

```python
demo.launch(share=True)
```

_Note: The share link expires after 72 hours._

### Permanent Hosting on Hugging Face Spaces

Deploy your app permanently (with free hosting and GPU support) on [Hugging Face Spaces](https://huggingface.co/spaces):

```bash
gradio deploy
```

> **IMPORTANT:** To proceed, you'll need an access token with **Write** permission on Hugging Face. If you haven't generated one yet, please [create one here](https://huggingface.co/settings/tokens).

Optionally, a GitHub Action will be configured to automatically update your Hugging Face repository on every push by adding your Hugging Face token as the `hf_token` secret in your repository.

Project URL on Hugging Face:  
[https://huggingface.co/spaces/layers2024/gradio-demo](https://huggingface.co/spaces/layers2024/gradio-demo)

## Gradio Python Client Example

The Gradio Python client simplifies using any Gradio app as an API. For example, consider a Hugging Face Space that transcribes audio files. With the `gradio_client` library, you can programmatically send audio files for transcription.

### Example: Transcribing Audio

1. **Record a 10-Second Audio Clip:**

   ```bash
   cd client
   arecord -f cd -d 10 -r 44100 -c 2 audio_sample.wav
   ```

2. **Run the Client Script to Transcribe Audio:**

   ```bash
   python whisper_app.py
   ```

### Full Python Client Code

Below is an example that demonstrates how to use the Gradio Python client:

```python
from gradio_client import Client, handle_file

# Connect to the Gradio app hosted on Hugging Face Spaces.
client = Client("abidlabs/whisper")

# Use the client to predict/transcribe the audio.
output = client.predict(audio=handle_file("audio_sample.wav"))
print(output)
```

## References & Resources

- [Gradio GitHub Repository](https://github.com/gradio-app/gradio)
- [Gradio Documentation](https://gradio.app/)
- [Gradio Components](https://www.gradio.app/docs/gradio/introduction)
- [Getting Started with the Gradio Python Client](https://www.gradio.app/guides/getting-started-with-the-python-client)
