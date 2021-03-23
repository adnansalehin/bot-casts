from os import path
import datetime


def get_audio_path(filename):
    return path.relpath('audio-output/{}.mp3'.format(filename))


def get_script_path(filename):
    return path.relpath('script-input/{}.txt'.format(filename))


def get_date_time():
    return "_" + str(datetime.datetime.utcnow()).replace(" ", "_").replace(":", ".")
