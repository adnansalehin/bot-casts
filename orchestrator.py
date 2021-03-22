from speech_synthesizer import start_speech_synthesis_from_text, download_from_s3_by_file_key

text = "This is Kevin running from the orchestrator script"
filename = "test"

file_key = start_speech_synthesis_from_text(text)

download_from_s3_by_file_key(file_key, filename)
