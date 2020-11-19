# Import pytube 
# Don't forgrt tp pip install pr pip3 install pytube 

import pytube

# create an input field for the user to type in the youtube video url
video_url = input("Type in the url and press enter : ") 
print('Your video will be in the current working directory / Downloads once done the window will close itself.')
# pass the url to pytube as a parameter of  pytube's YouTube method 
youtube = pytube.YouTube(video_url)

# Download the video over stream and store in video variable
video = youtube.streams.first()

 # path where the video should be installed
video.download('./Downloads')

# Viola Done!!
