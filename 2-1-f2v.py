# code to take a folder of images to convert it into a video

import cv2
import os

path_input_dir = "frames/"
video = "2.mp4"
frame_rate = 60


def frames_to_video(path_input_dir, video, frame_rate):
    # path to the folder with images
    images = []
    for img in os.listdir(path_input_dir):
        if img.endswith(".jpg"):
            images.append(img)

    # sort images based on their numerical order
    images.sort(key=lambda x: int(x[:-4]))

    # get image dimensions
    img = cv2.imread(os.path.join(path_input_dir, images[0]))
    height, width, layers = img.shape

    # create video writer object
    video = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))

    # loop through images and write them to video
    for image in images:
        img_path = os.path.join(path_input_dir, image)
        frame = cv2.imread(img_path)
        video.write(frame)

    # release video writer
    video.release()
    cv2.destroyAllWindows()

# function call
frames_to_video(path_input_dir, video, frame_rate)
