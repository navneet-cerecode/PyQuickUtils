import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from ttkthemes import ThemedTk
from tkinter import ttk

def remove_vocals(input_audio, output_folder="output"):
    """
    Removes vocals from an input song using Demucs and saves the instrumental version.
    """
    os.makedirs(output_folder, exist_ok=True)
    
    command = f'demucs --two-stems=vocals "{input_audio}"'
    subprocess.run(command, shell=True)
    
    song_name = os.path.basename(input_audio).split('.')[0]
    instrumental_path = os.path.join("separated/htdemucs", song_name, "no_vocals.wav")
    
    messagebox.showinfo("Success", f"Instrumental saved at: {instrumental_path}")
    return instrumental_path

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav;*.flac")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def process_audio():
    input_song = entry_path.get()
    if not input_song:
        messagebox.showerror("Error", "Please select an audio file")
        return
    remove_vocals(input_song)

# Create GUI window
root = ThemedTk(theme="arc")
root.title("Karaoke Maker")
root.geometry("500x250")

# Title Label
ttk.Label(root, text="Karaoke Maker", font=("Arial", 16, "bold")).pack(pady=10)

# File Selection
frame = ttk.Frame(root)
frame.pack(pady=10)

entry_path = ttk.Entry(frame, width=40)
entry_path.pack(side=tk.LEFT, padx=5)

btn_browse = ttk.Button(frame, text="Browse", command=browse_file)
btn_browse.pack(side=tk.LEFT)

# Process Button
btn_process = ttk.Button(root, text="Remove Vocals", command=process_audio)
btn_process.pack(pady=20)

# Run GUI
root.mainloop()