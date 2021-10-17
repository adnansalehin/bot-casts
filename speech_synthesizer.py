import time
import boto3
import utils

# Let's use Amazon S3
S3_KEY_PREFIX = 'kevin-speaks'
S3_BUCKET_NAME = 'audios-from-polly'
s3 = boto3.client('s3')
client = boto3.client('polly')


def start_speech_synthesis_from_text(text):
    response = client.start_speech_synthesis_task(
        Engine='neural',
        LanguageCode='en-US',
        OutputFormat='mp3',
        OutputS3BucketName=S3_BUCKET_NAME,
        OutputS3KeyPrefix=S3_KEY_PREFIX,
        Text=text,
        TextType='text',
        VoiceId='Kevin'
    )

    audio_uri = response["SynthesisTask"]["OutputUri"]
    task_id = response["SynthesisTask"]["TaskId"]
    status = response["SynthesisTask"]["TaskStatus"]
    print("uri:", audio_uri)

    while status == "scheduled" or status == "inProgress":
        status = client.get_speech_synthesis_task(TaskId=task_id)["SynthesisTask"]["TaskStatus"]
        if status == "scheduled" or status == "inProgress":
            print("status is:", status, "sleeping for 15 seconds")
            time.sleep(15)
    print("Task finished with status: ", status)

    return get_key_from_uri(audio_uri)


def download_from_s3_by_file_key(file_key, filename):
    print('trying to download file:', file_key)

    with open(utils.get_audio_path(filename), 'wb') as data:
        s3.download_fileobj('audios-from-polly', file_key, data)


def get_key_from_uri(uri):
    return S3_KEY_PREFIX + uri.split(S3_KEY_PREFIX)[1]


