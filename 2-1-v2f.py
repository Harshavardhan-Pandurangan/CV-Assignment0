# code to take a video and convert it into frames

import cv2
import os

video = "1.mp4"
path_output_dir = "frames"


def video_to_frames(video, path_output_dir):
    # video given at path video
    video = cv2.VideoCapture(video)

    # open the video and read the first frame
    if video.isOpened():
        ret, frame = video.read()
        count = 0
    else:
        ret = False

    # create directory if it doesn't exist
    if not os.path.exists(path_output_dir):
        os.makedirs(path_output_dir)

    # read and save each frame in the video
    while ret:
        cv2.imwrite(path_output_dir + "/%d.jpg" % count, frame)
        ret, frame = video.read()
        count += 1


# function call
video_to_frames(video, path_output_dir)
