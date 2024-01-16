# code to combine two videos (chroma key)

import cv2
import os

fg_video = "fg.mp4"
bg_video = "bg.mp4"
output_video = "output.mp4"

# create folders to store frames
path_input_fg_dir = "fg_frames/"
os.makedirs(path_input_fg_dir, exist_ok=True)
path_input_bg_dir = "bg_frames/"
os.makedirs(path_input_bg_dir, exist_ok=True)
path_output_dir = "output_frames/"
os.makedirs(path_output_dir, exist_ok=True)

# function to extract frames from a video
def video_to_frames(video, path_output_dir):
    video = cv2.VideoCapture(video)

    if video.isOpened():
        ret, frame = video.read()
        count = 0
    else:
        ret = False

    if not os.path.exists(path_output_dir):
        os.makedirs(path_output_dir)

    while ret:
        cv2.imwrite(path_output_dir + "/%d.jpg" % count, frame)
        ret, frame = video.read()
        count += 1

# function call
video_to_frames(fg_video, path_input_fg_dir)
video_to_frames(bg_video, path_input_bg_dir)

# function to combine two videos (chroma key)
def chroma_key(fg_video, bg_video, output_video, thresh):
    fg_path = "fg_frames/"
    bg_path = "bg_frames/"
    output_path = "output_frames/"

    # Open background and foreground videos
    fg_cap = cv2.VideoCapture(fg_video)
    bg_cap = cv2.VideoCapture(bg_video)

    # Get video properties
    width = int(fg_cap.get(3))
    height = int(fg_cap.get(4))
    fps = fg_cap.get(5)

    # Create VideoWriter object for output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    try:
        while True:
            ret_fg, fg_frame = fg_cap.read()
            ret_bg, bg_frame = bg_cap.read()

            if not ret_fg or not ret_bg:
                break

            # HSV for chroma keying (better for color detection)
            hsv_frame = cv2.cvtColor(fg_frame, cv2.COLOR_BGR2HSV)

            # threshold for chroma key color
            lower_bound = (40, 40, 40)
            upper_bound = (80, 255, 255)

            mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

            inverted_mask = cv2.bitwise_not(mask)

            fg = cv2.bitwise_and(fg_frame, fg_frame, mask=inverted_mask)
            bg = cv2.bitwise_and(bg_frame, bg_frame, mask=mask)

            # combine foreground and background
            result_frame = cv2.add(fg, bg)

            out_video.write(result_frame)

            cv2.imshow('Chroma Keying', result_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        fg_cap.release()
        bg_cap.release()
        out_video.release()
        cv2.destroyAllWindows()

# function call
chroma_key(fg_video, bg_video, output_video, thresh=40)
