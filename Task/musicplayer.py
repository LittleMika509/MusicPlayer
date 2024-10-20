import pygame
import tkinter
from tkinter import filedialog


pygame.mixer.init()

root = tkinter.Tk()
root.title("Music Player")

def play_song():
    song = filedialog.askopenfilename(filetypes = [("Audio Files", "*.mp3")])
    if song:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.unpause()

def stop_song():
    pygame.mixer.music.stop()

play_button = tkinter.Button(root, text="Play", command = play_song)
play_button.pack(pady=10)

pause_button = tkinter.Button(root, text="Pause", command = pause_song)
pause_button.pack(pady=10)

resume_button = tkinter.Button(root, text="Resume", command = resume_song)
resume_button.pack(pady=10)

stop_button = tkinter.Button(root, text="Stop", command = stop_song)
stop_button.pack(pady=10)

root.mainloop()
