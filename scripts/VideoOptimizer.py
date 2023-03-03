# 视频优化
# 使用 Python 来优化视频，还可以使用它来优化图像。该脚本使用 Moviepy 模块，允许你修剪、添加音频、设置视频速度、添加 VFX 等等。
# pip install moviepy
import moviepy.editor as pyedit
# Load the Video
video = pyedit.VideoFileClip("vid.mp4")
# Trimming
vid1 = video.subclip(0, 10)
vid2 = video.subclip(20, 40)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Speed up the video
final_vid = final_vid.speedx(2)
# Adding Audio to the video
aud = pyedit.AudioFileClip("bg.mp3")
final_vid = final_vid.set_audio(aud)
# Reverse the Video
final_vid = final_vid.fx(pyedit.vfx.time_mirror)
# Merge two videos
vid1 = pyedit.VideoFileClip("vid1.mp4")
vid2 = pyedit.VideoFileClip("vid2.mp4")
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Add VFX to Video
vid1 = final_vid.fx(pyedit.vfx.mirror_x)
vid2 = final_vid.fx(pyedit.vfx.invert_colors)
final_vid = pyedit.concatenate_videoclips([vid1, vid2])
# Add Images to Video
img1 = pyedit.ImageClip("img1.jpg")
img2 = pyedit.ImageClip("img2.jpg")
final_vid = pyedit.concatenate_videoclips([img1, img2])
# Save the video
final_vid.write_videofile("final.mp4")