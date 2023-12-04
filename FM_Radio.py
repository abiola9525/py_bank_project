import tkinter as tk
import tkinter.filedialog
import pygame
import time

class MusicPlayer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Music Player")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.paused = False
        self.volume = 0.5
        self.current_time = 0
        self.total_time = 0
        self.song = None
        self.file_path = None
        self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL, label="Volume", command=self.update_volume)
        self.volume_scale.set(0.5)
        self.volume_scale.pack(pady=10)
        self.time_label = tk.Label(self.root, text="0:00 / 0:00")
        self.time_label.pack()
        self.progress_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, showvalue=False, command=self.update_time)
        self.progress_scale.pack(fill="x", padx=10)
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=10)
        self.open_button = tk.Button(self.control_frame, text="Open", command=self.select_file)
        self.open_button.pack(side="left")
        self.play_button = tk.Button(self.control_frame, text="Play", command=self.play)
        self.play_button.pack(side="left", padx=10)
        self.stop_button = tk.Button(self.control_frame, text="Stop", command=self.stop)
        self.stop_button.pack(side="left")

    def select_file(self):
        self.file_path = tk.filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(self.file_path)
            self.total_time = pygame.mixer.Sound(self.file_path).get_length()
            self.progress_scale.config(to=self.total_time)
            self.time_label.config(text="0:00 / " + self.format_time(self.total_time))

    def play(self):
        if self.file_path:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.play()
                self.current_time = 0
                self.paused = False
                self.update_time_scale()

    def stop(self):
        if self.file_path:
            pygame.mixer.music.stop()
            self.current_time = 0
            self.paused = False
            self.update_time_scale()

    def update_volume(self, volume):
        self.volume = float(volume)
        pygame.mixer.music.set_volume(self.volume)

    def update_time(self, value):
        self.current_time = float(value)
        pygame.mixer.music.play(start=self.current_time)
        self.update_time_scale()

    def update_time_scale(self):
        self.progress_scale.set(self.current_time)
        self.time_label.config(text=self.format_time(self.current_time) + " / " + self.format_time(self.total_time))

    def format_time(self, time):
        minutes = int(time // 60)
        seconds = int(time % 60)
        return "{:d}:{:02d}".format(minutes, seconds)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    music_player = MusicPlayer()
    music_player.run()
