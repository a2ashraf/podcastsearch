from youtube_transcript_api import YouTubeTranscriptApi
import json

def load_data(video_id, keyword):
    # Use a breakpoint in the code line below to debug your script.
    data = YouTubeTranscriptApi.get_transcript(video_id)
    for item in data:
        # print(item)
        if keyword in item['text']:
            print(item['text'])
            timing = item['start']
            print(timing)
            output = f'https://youtu.be/{video_id}?t={int(timing)}'
            print(output)


load_data("ppBsW6RhYKI", "disputed")
