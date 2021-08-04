from googleapiclient.discovery import build
import collections
import config

api_key = config.api
  
  
def video_comments(video_id):

    channels_comments = collections.defaultdict(int)
    old_comments = [] #гКод
  
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
  
    video_response=youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id,

    ).execute()
  
    while video_response:

        for item in video_response['items']:
                       
            channel_id = item['snippet']['topLevelComment']['snippet']['authorChannelId']['value']

            if channels_comments[channel_id] <= 3:
                comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
                if comment not in old_comments: #гКод
                    print(channel_id) #Debug вывод id канала

                    if "залайкайте" not in comment.lower() and "полдишесшя" not in comment.lower() and "подпишешся" not in comment.lower() and "лайк" not in comment.lower():
        	            print(comment, end = '\n\n')
                    channels_comments[channel_id] += 1
                    old_comments.append(comment)
      
       
  
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                    part = 'snippet,replies',
                    videoId = video_id
                ).execute()
        else:
            break
  
video_id = "HT_IyPyla94" #id видео
  
video_comments(video_id)
