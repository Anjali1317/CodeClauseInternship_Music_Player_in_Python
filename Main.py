import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        
        self.playlist = []
        self.current_track = 0
        
        pygame.init()
        pygame.mixer.init()
        
        self.create_ui()
    
    def create_ui(self):
        self.track_label = tk.Label(self.root, text="No Track")
        self.track_label.pack(pady=50)
        
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)
        
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)
        
        self.load_button = tk.Button(self.root, text="Load Music", command=self.load_music)
        self.load_button.pack(pady=10)
    
    def load_music(self):
        file_paths = filedialog.askopenfilenames(title="Select Music", filetypes=[("Audio files", "*.mp3 *.wav")])
        if file_paths:
            self.playlist = file_paths
            self.current_track = 0
            self.play_music()
    
    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()
            self.track_label.config(text=f"Playing: {self.playlist[self.current_track]}")
    
    def pause_music(self):
        pygame.mixer.music.pause()
    
    def stop_music(self):
        pygame.mixer.music.stop()
        self.track_label.config(text="No Track")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    music_player.run()
