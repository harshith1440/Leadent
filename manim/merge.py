from moviepy import VideoFileClip, AudioFileClip

video = VideoFileClip("media/videos/test/1080p60/RationalIntro.mp4")
audio = AudioFileClip("introRat.mp3")

# 🔥 FIX TIMING HERE
if audio.duration > video.duration:
    audio = audio.subclipped(0, video.duration)  # ✅ fixed
else:
    video = video.with_duration(audio.duration)

# Merge
final = video.with_audio(audio)

final.write_videofile("final_output.mp4")