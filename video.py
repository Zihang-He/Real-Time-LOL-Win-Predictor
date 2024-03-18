from moviepy.editor import ImageSequenceClip
import os

frames_dir = './frames/'

frame_files = sorted([frames_dir + f for f in os.listdir(frames_dir) if f.endswith('.png')])
clip = ImageSequenceClip(frame_files, fps=10)  # fps can be adjusted for desired speed
video_path = './frames/probabilities_video.mp4'
clip.write_videofile(video_path)