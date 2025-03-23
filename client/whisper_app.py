from gradio_client import Client, handle_file

client = Client("abidlabs/whisper")

transcription = client.predict(
    audio=handle_file("audio_sample.wav")
)

print(transcription)
