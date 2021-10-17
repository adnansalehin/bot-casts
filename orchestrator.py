import script_generator
import speech_synthesizer
import utils

SUBREDDIT = "nosleep"
FILENAME = SUBREDDIT + utils.get_date_time()


''' script collection '''

script_generator.download_top_n_posts(subreddit=SUBREDDIT, filename=FILENAME, period="week", skip=0, limit=1)
path = utils.get_script_path(filename=FILENAME)
with open(path, 'r', encoding="utf-8") as f:
    script = f.read()


''' script to speech conversion '''

file_key = speech_synthesizer.start_speech_synthesis_from_text(text=script)

speech_synthesizer.download_from_s3_by_file_key(file_key=file_key, filename=FILENAME)
