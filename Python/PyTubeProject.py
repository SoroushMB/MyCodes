from pytube import YouTube
link = input("EnterYourYoutubeURL: ")
yt = YouTube(link)
videos = yt.streams.all()
video  =list(enumerate(videos))
for i in video:
    print(i)

print("EnterTheDesiredOptionToDownload: ")
dn_option = int(input(" EnterTheOption: "))
dn_video = videos[dn_option]
dn_video.download()

print(" DownloadedSuccesfully! ")