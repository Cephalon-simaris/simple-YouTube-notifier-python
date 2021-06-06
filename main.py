from googleapiclient.discovery import build
import time
global current
global beforelink

api_key = "inset api key here"

youtube = build('youtube','v3',developerKey=api_key)

def uploadcheck(beforelink,afterlink):
    if beforelink == afterlink:
        return 0
    else:
        beforelink = afterlink
        return afterlink
while True:
    request1 = youtube.activities().list(
        part="contentDetails",
        channelId="insert channel id here"
    )

    response1 = request1.execute()

    before = response1['items'][0]['contentDetails']['upload']['videoId'] #initial link
    time.sleep(10)
    request2 = youtube.activities().list(
        part="contentDetails",
        channelId="insert channel id here"
    )

    response2 = request2.execute()

    after = response2['items'][0]['contentDetails']['upload']['videoId'] #link after 10 seconds
    a = uploadcheck(before,after)
    if a == 0:
        print("same video")
        #do stuff here
    else:
        print("New video uploaded!")
        #do stuff here
    time.sleep(10)
