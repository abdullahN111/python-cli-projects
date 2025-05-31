from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4")
        high_resolution = stream.get_highest_resolution()

        high_resolution.download(output_path=save_path)
        print("Video downloaded successfully.")
    except Exception as e:
        print(e)
        print("Something went wrong.")


url = "https://youtu.be/Y8Tko2YC5hA?si=Jxfjyi3dyVocAeJE"
save_path = "C:/Users/uni-tech/Downloads"

download_video(url, save_path)