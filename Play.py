import os
import tkinter as tk
import sys
import random
from tkinter import messagebox
import webbrowser
import ctypes

try:
    import vlc
except ImportError:
    ctypes.windll.user32.MessageBoxW(0, "We need vlc to run, please download it..\n")
    webbrowser.open("https://www.videolan.org/vlc/")
    sys.exit()
video_folder = "Videos"
video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

if not video_files:
    messagebox.showerror(
        "Error",
        "Can't find your video. Please put your video in folder 'Videos', only accept mp4 type",
    )
    sys.exit(1)


playing = random.choice(video_files)
path = os.path.join(video_folder, playing)
print(f"Playing: {path}")
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(path)
player.set_media(media)
player.set_fullscreen(True)
root = tk.Tk()
root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", lambda: None)


def check_end():
    if player.is_playing():
        root.after(1000, check_end)
    else:
        root.destroy()


player.play()
root.after(1000, check_end)
root.mainloop()
